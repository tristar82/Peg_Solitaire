# Creates the necessary classes to run the peg solitaire game (from main.py)

from rich.console import Console
from rich.table import Table
from copy import copy
import os
import datetime

class Peg:
    def __init__(self):
        self.legal_moves_list = []

        self.direction_dict = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

    def import_from_file(self):
        '''Function to load in saved moved from a text file. Assumes file in current working directory'''
        while True:
            try:
                with open(input("Enter solution filename in full: "), 'r') as import_file:
                    file_contents = import_file.read()
                    import_file.close()
                    file_contents_clean = file_contents.strip().split(',')
                    print("Solution file containing {} moved located and opened successfully".format(
                        len(file_contents_clean)))
                    return file_contents_clean

            except OSError as e:
                print("Error - Solution file not imported successfully", e)

    def update_board_pegs(self, org_coords, move_direction, dest_coords, board):
        '''
        Function to update the board when a successful move is made by the user i.e. origin 
        and middle pegs are removed and desintation is filled.

        Parameters
        ----------
        org_coords: list (2 elements)
            Origin location coordinates in [row, col] format

        move_direction: str(1)
            Direction from origin to destination (i.e. (U)p, (D)own, (Left), (R)ight).

        dest_coords: list (2 elements)
            Destination location coordinates in [row, col] format

        board: 
            Current state of playing board

        '''
        # origin hole to be emptied
        board[org_coords[0]][org_coords[1]] = False

        # middle coords updated
        board[org_coords[0] + self.direction_dict[move_direction][0]][org_coords[1] 
            + self.direction_dict[move_direction][1]] = False

        # destination filled
        board[dest_coords[0]][dest_coords[1]] = True

    def validated_middle_peg(self, org_coords, dest_coords):
        '''
        Function to verify origin to destination direction, 
        ensure the origin and destination are 2 pegs away from one another 
        and to calculated the coordinated of the middle peg (between origin and destination)

        Parameters
        ----------
        org_coords: list (2 elements)
            Origin location coordinates in [row, col] format

        dest_coords: list (2 elements)
            Destination location coordinates in [row, col] format

        Returns
        -------
        3 elements
            Element 1 (index 0) is a list with the coordinates of the 
                character entered, in the format [row,col]
            Element 2 (index 1) is the final character selected (as may 
                be different as the input character, due to error handling)
            Element 3 (index 2) is a list with the coordinates of the 
                middle peg position determined, in the format [row,col]
        '''
        move_direction = None
        result = None
        middle_peg_pos = None

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
            middle_peg_pos = [org_coords[0] + self.direction_dict[move_direction][0],
                              org_coords[1] + self.direction_dict[move_direction][1]]
        except:
            middle_peg_pos = [9,9] #i.e. error
        
        return result, move_direction, middle_peg_pos

    def add_move(self, org_char, dest_char):
        '''Appends legal moves to a list for export i.e. ox for a move of peg from position o to position x'''
        self.legal_moves_list.append([org_char, dest_char])

    def verify_input_char(self, input_char, peg_dict, location):
        '''
        Function to verify if a character peg position is valid and has a corresponding set of peg coordinates.
        Includes error handling in case that the an invalid (non-existing) peg character is entered by the user.

        Parameters
        ----------
        input_char: str(1)
            Single alpha character (a-p,A-P,x)

        peg_dict: str
            Name of dictionary variable containing the character to position coords lookup

        location: str
            String to indentify if the position entered is the origin or destination. 
            Used for more descriptive error messages

        Returns
        -------
        results: tuple of 2 elements
            Element 1 (index 0) is a list with the coordinates of the 
                        character entered, in the format [row,col]
            Element 2 (index 1) is the final character selected (as may 
                        be different as the input character, due to error handling)
        '''
        while input_char not in peg_dict.keys():
            input_char = input(
                'Please enter a single character position for {} as found on the board: '.format(location.upper()))
        return peg_dict[input_char], input_char

    def auto_export_to_file(self):
        '''
        Exports the legal moves made during the game into a text file (in CSV format).
        Filename autogenerated based on the date time that the export occurs.
        '''
        while True:
            try:
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
        # setting up the board from a list of lists
        self.board = [[not row == ele == 3 if ele in [2, 3, 4] or row in [2, 3, 4] 
                        else None for row in range(7)] for ele in range(7)]

        # Generate a list of characters to represent peg positions (a-p,x,P-A)
        a_to_p = [chr(i) for i in range(97, 113)]
        self.peg_chars = a_to_p + ['x'] + [i.upper() for i in a_to_p[::-1]]

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

        # Create a dictionary that determines relative coordinate 
        # adjustments based on the direction from the origin to destination.
        self.direction_dict = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}        

    def print_board(self, pegs_on_board):
        '''
        Function that prints the current state of the board (i.e. pegs and holes). 
        Also prints the numner of pegs remaining on the board
        '''
        board = self.board
        
        # Creates a visual representation of the board from the list of 
        # lists (of None, True, False) - found in __init__
        board_viz = {None: ' ', True: 'X', False: '.'}
        display_board = []
        for row in board:
            display_board_sub = []
            for col in row:
                display_board_sub.append(board_viz[col])
            display_board.append(display_board_sub)

        # Sets up the table 
        heading_text = "{} Pegs Remaining on Board".format(pegs_on_board)
        table = Table(title=heading_text, show_lines=True)

        table.add_column(" ")

        for i in range(7):
            table.add_column(str(i), justify='right', style="cyan", no_wrap=True)

        # Assinging a variable named 'view' of the rows (and columns) created above
        view = copy(display_board)

        # Adding rows to rich table
        for row_i in range(7):
           table.add_row(str(row_i), *display_board[row_i])

        # Displaying the rich table
        console = Console()
        console.print(table)

    def print_map(self, peg_pos_dict):
        '''
        Function that prints the map of peg positions relative to the playing board. 
        Uses the peg position dictionary
        '''
        table = Table(title="Solitaire Peg Board Character Map", show_lines=True)

        table.add_column(" ")

        for i in range(7):
            table.add_column(str(i), justify='right', style="cyan", no_wrap=True)

        # This loop creates an empty 7x7 table
        pegs_col = []
        pegs_row = []

        for row in range(7):
            for col in range(7):
                pegs_col.append(" ")
            pegs_row.append(pegs_col)
            pegs_col = []

        # The empty 7x7 table (created above) is now populated with peg characters
        for letter in self.peg_pos_dict.keys():
            pegs_row[self.peg_pos_dict[letter][0]][self.peg_pos_dict[letter][1]] = letter

        # Assinging a variable named 'view' of the rows (and columns) created above
        view = copy(pegs_row)

        # Adding rows to rich table
        for row_i in range(7):
            table.add_row(str(row_i), *pegs_row[row_i])

        # Displaying the rich table
        console = Console()
        console.print(table)

    def is_middle_filled(self, org_coords, board, move_direction):
        '''
        Function to check if middle peg hole is empty. 
        Uses origin peg coordinate and move direction to determine
        '''
        return board[org_coords[0] + self.direction_dict[move_direction][0]]\
            [org_coords[1] + self.direction_dict[move_direction][1]]

    def is_destination_empty(self, destination_peg_coords, board):
        '''Function to check if destination peg hole is empty'''
        return not board[destination_peg_coords[0]][destination_peg_coords[1]] in [None, True]

    def is_origin_filled(self, origin_peg_coords, board):
        '''Function to check if origin peg hole is empty'''
        return not board[origin_peg_coords[0]][origin_peg_coords[1]] in [None, False]

class Menu:
    def display_welcome(self):
        '''Display's Welcome Message when game is loaded'''
        print("Welcome to Peg Solitaire")

    def rules(self):
        print("The rules of the game are...\n" 
              "* Peg solitaire is a game for one player. There are 33 pegs \n"
              " arranged in a 'plus' symbol configuration.\n"
              "* The peg in the centre is removed. This leaves 32 pegs.\n"
              "* The objective of the game is to end up with one peg in the middle hole. \n"
              "* This is achieved by removing one peg at a time by jumping an adjacent \n"
              " peg over it into an adjacent empty hole in the other side.\n"
              "* For example, the peg marked with a cross would be removed by \n"
              " jumping the peg marked with a triangle into the hole in \n"
              " the centre (shaded). \n"
              "* No diagonal jumps are permitted.\n"
              "* You can exit the game during play by typing 'EXIT'\n\n"
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