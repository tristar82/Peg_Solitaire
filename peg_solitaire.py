from rich.console import Console
from rich.table import Table
from copy import copy
import os
import datetime

class Peg:
    def __init__(self):
        self.legal_moves_list = []

    def import_from_file(self):
        '''

        :return:
        '''
        while True:
            try:
                with open(input("Enter solution filename in full: "), 'r') as import_file:
                    file_contents = import_file.read()
                    import_file.close()
                    file_contents_clean = file_contents.strip().split(',')
                    print("Solution file containing {} moved located and opened successfully".format(
                        len(file_contents_clean)))
                    return file_contents_clean
                    break
            except OSError as e:
                print("Error - Solution file not imported successfully", e)

    def update_board_pegs(self, org_coords, move_direction, dest_coords, board):
        '''
        When a move is successful - update all the pegs (origin, middle, destination)
        :param org_coords:
        :param dest_coords:
        :param middle_coords:
        :param board:
        :return:
        '''
        # origin to be emptied
        board[org_coords[0]][org_coords[1]] = False

        # middle coords updated
        direction_dict = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

        board[org_coords[0] + direction_dict[move_direction][0]][org_coords[1] + direction_dict[move_direction][1]] = False

        # destination filled
        board[dest_coords[0]][dest_coords[1]] = True

    def validated_middle_peg(self, org_coords, dest_coords):
        '''
        Performs the jobs of: UDLR, is_two_away and middle_peg_coords
        :param peg_coords:
        :param dest_coords:
        :return:
        '''
        direction_dict = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
        move_direction = ''
        result = ''
        middle_peg_pos = ''

        if org_coords[0] == dest_coords[0]: # same row
            if abs(org_coords[1] - dest_coords[1]) == 2: # col is +/- 2
                if org_coords[1] - dest_coords[1] < 0:
                    move_direction = 'R' # right
                    result = True

                else:
                    move_direction = 'L' # left
                    result = True

            else:
                result =  False
        elif abs(org_coords[0] - dest_coords[0]) == 2:
            if org_coords[0] - dest_coords[0] < 0:
                move_direction = 'D'  # down
                result = True

            else:
                move_direction = 'U'  # up
                result = True

        else:
            result = False

        try:
            middle_peg_pos = [org_coords[0] + direction_dict[move_direction][0],
                              org_coords[1] + direction_dict[move_direction][1]]
        except:
            pass
        return result, move_direction, middle_peg_pos

    def add_move(self, org_char, dest_char):
        '''
        Append legal moves to a list for export i.e. ox for a move of peg from position o to position x
        :param origin_destination: str(2)
        :return:
        '''
        self.legal_moves_list.append([org_char, dest_char])

    def verify_input_char(self, input_char, peg_dict, location):
        '''
        Determines the board coordinates of a character.
        Includes error handling in case the character entered is not present on the board

        Parameters
        ----------
        input_char: str(1)
            Single alpha character (a-p,A-P,x)

        peg_dict: str
            Name of variable containing dictionary with character to position coords lookup

        location: str
            String to indentify if the position entered is the origin or destination

        Returns
        -------
        results: tuple of 2 elements
            Element 1 (index 0) is a list with the coordinates of the character entered, in the formar [row,col]
            Element 2 (index 1) is the final character selected (as may be different due to error handling)
        '''
        while input_char not in peg_dict.keys():
            input_char = input(
                'Please enter a single character position for {} as found on the board: '.format(location.upper()))
        return peg_dict[input_char], input_char

    def auto_export_to_file(self):
        '''
        Exports the legal, saved moves to a text file

        Parameters
        ----------
        input_char: str(1)
            Single alpha character (a-p,A-P,x)

        peg_dict: str
            Name of variable containing dictionary with character to position coords lookup

        location: str
            String to indentify if the position entered is the origin or destination

        Returns
        -------
        results: tuple of 2 elements
            Element 1 (index 0) is a list with the coordinates of the character entered, in the formar [row,col]
            Element 2 (index 1) is the final character selected (as may be different due to error handling)
        '''


        while True:
            try:
                #file_name = input("Enter export solution filename in full: ")
                #if os.path.isfile(file_name):
                    #print("This filename existed and was overwritten")
                now_dt = datetime.datetime.now()
                date_time = now_dt.strftime("%Y_%m_%d__%H_%M")
                export_file_name = 'legal_moves_output_{}.txt'.format(date_time)
                with open(export_file_name, 'w') as f:
                    for num, item in enumerate(self.legal_moves_list):
                        if num == len(self.legal_moves_list) - 1:
                            f.write(''.join(item))
                        else:
                            f.write(''.join(item) + ',')
                    break

            except OSError as e:
                print("Error - Solution file not exported successfully", e)

class Board:
    def __init__(self):
        # setting up the board
        self.board = [[not row == ele == 3 if ele in [2, 3, 4] or row in [2, 3, 4] else None for row in range(7)] for
                      ele in range(7)]

        # Get peg chars
        a_to_p = [chr(i) for i in range(97, 113)]
        self.peg_chars = a_to_p + [chr(120)] + [i.upper() for i in a_to_p[::-1]]

        # generate char to coordinates lookup dictionary
        peg_pos_idx = 0
        peg_position_dict = {}

        for row_num, row in enumerate(self.board):
            for col_num, ele in enumerate(row):
                if ele == None:
                    pass

                else:
                    peg_position_dict[self.peg_chars[peg_pos_idx]] = [row_num, col_num]
                    peg_pos_idx += 1

        self.peg_pos_dict = peg_position_dict        

    # def character_lookup(self):
    #     '''
    #     Purpose of this XXX is to create the dictionary of position characters to board coordinates
    #     '''
    #     # char lookup
    #     peg_pos_idx = 0
    #     peg_position_dict = {}

    #     for row_num, row in enumerate(self.board):
    #         for col_num, ele in enumerate(row):
    #             if ele == None:
    #                 pass

    #             else:
    #                 peg_position_dict[self.peg_chars[peg_pos_idx]] = [row_num, col_num]
    #                 peg_pos_idx += 1

    #     self.peg_pos_dict = peg_position_dict

    def print_board(self, pegs_on_board):
        board = self.board;
        board_viz = {None: ' ', True: 'X', False: '.'}
        display_board = []

        for row in board:
            display_board_sub = []
            for col in row:
                display_board_sub.append(board_viz[col])
            display_board.append(display_board_sub)

        heading_text = "{} Pegs Remaining on Board".format(pegs_on_board)
        #table = Table(title="Solitaire Peg Board", show_lines=True)
        table = Table(title=heading_text, show_lines=True)

        table.add_column(" ")

        for i in range(7):
            table.add_column(str(i), justify='right', style="cyan", no_wrap=True)

        # view of the pegs displayed on board
        view = copy(display_board)

        # add rows to rich table
        for row_i in range(7):
           table.add_row(str(row_i), *display_board[row_i])

        # show rich table
        console = Console()
        console.print(table)

    def print_map(self, peg_pos_dict):

        table = Table(title="Solitaire Peg Board Character Map", show_lines=True)

        table.add_column(" ")

        for i in range(7):
            table.add_column(str(i), justify='right', style="cyan", no_wrap=True)

        pegs_sub = []
        pegs = []

        for row in range(7):
            for col in range(7):
                pegs_sub.append(" ")
            pegs.append(pegs_sub)
            pegs_sub = []

        for letter in self.peg_pos_dict.keys():
            pegs[self.peg_pos_dict[letter][0]][self.peg_pos_dict[letter][1]] = letter

        # view of the pegs displayed on board
        view = copy(pegs)

        # add rows to rich table
        for row_i in range(7):
            table.add_row(str(row_i), *pegs[row_i])

        # show rich table
        console = Console()
        console.print(table)

    def is_middle_filled(self, org_coords, board, move_direction):
        '''
        Determines if middle peg is empty
        Direction is (U)p, (D)own, (L)eft or (R)ight
        '''
        direction_dict = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

        if board[org_coords[0] + direction_dict[move_direction][0]][
            org_coords[1] + direction_dict[move_direction][1]]:
            return True
        else:
            return False

    def is_destination_empty(self, destination_peg_coords, board):
        '''Function to check if destination peg hole is empty'''
        # if board[destination_peg_coords[0]][destination_peg_coords[1]] in [None, True]:
        #     return False
        # else:
        #     return True
        return not board[destination_peg_coords[0]][destination_peg_coords[1]] in [None, True]


    def is_origin_filled(self, origin_peg_coords, board):
        '''Function to check if origin peg hole is empty'''
        # if board[origin_peg_coords[0]][origin_peg_coords[1]] in [None, False]:
        #     return False
        # else:
        #     return True
        return not board[origin_peg_coords[0]][origin_peg_coords[1]] in [None, False]

class Menu:
    def display_welcome(self):
        print("Welcome to Peg Solitaire")

    def rules(self):
        print("The rules of the game are...\n" +
              "Peg solitaire is a game for one player. There are 33 pegs arranged in a 'plus' symbol configuration.\n"+
              "The peg in the centre is removed. This leaves 32 pegs.\n"+
              "The objective of the game is to end up with one peg in the middle hole (x). \n"+
              "This is achieved by removing one peg at a time by jumping an adjacent peg over it into \n"+
              "an adjacent empty hole in the other side.\n"+
              "For example, the peg marked with a cross would be removed by jumping the peg marked with \n"+
              "a triangle into the hole in the centre (shaded). No diagonal jumps are permitted.\n"+
              "You can exit the game during play by typing 'EXIT'\n"+
              "Now lets play!!\n")

    def initiate_game(self):
        print("Options are (R)ules, Load (S)olution File, (P)lay game or (E)xit")
        valid_selection = False
        while valid_selection == False:
            user_selection_start = input("Please enter selection: ").upper()
            if user_selection_start in ['R','S','P','E']:
                return user_selection_start
                valid_selection = True
            else:
                print("Please enter a valid selection")