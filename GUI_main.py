# GUI Version of the Peg Solitaire Assignment - Advanced Section

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

import os
import datetime

from peg_solitaire import Board
from peg_solitaire import Peg
from peg_solitaire import Menu

menu = Menu()
peg = Peg()
board_ = Board()

global pegs_on_board
global state_of_play
global org_coords_input
global dest_coords_input

peg_pos_dict = board_.peg_pos_dict
game_started = False
pegs_on_board = 32
state_of_play = 0
org_coords_input = None
dest_coords_input = None

class Application(tk.Frame):
    def __init__(self, master):
        """This initializes the application frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.coords = []
        self.chars_copy = None
        self.base = [chr(i) for i in range(97, 113)]
        self.chars = self.base + ['x'] + [i.upper() for i in self.base[::-1]]
        self.create_grid_coords()
        self.create_widgets()
        self.board = board_.board
        self.user_org_coords = [9, 9]  # using for move validation when importing files
        self.user_dest_coords = [9, 9]  # using for move validation when importing files
        self.load_error_count = 0

    def display_label(self):
        '''Function to display number of pegs remaining'''
        tk.Label(text="{}".format(pegs_on_board),
                 font=("Helvetica", 14)).grid(row=7, column=0)

    def create_grid_coords(self):
        '''Function to create board grid coordinates for GUI'''
        raw_grid = [[not row == ele == 3 if ele in [2, 3, 4] or
                                            row in [2, 3, 4] else None for row in range(7)] for ele
                    in range(7)]
        for row in range(len(raw_grid)):
            for col in range(len(raw_grid[row])):
                if raw_grid[row][col] is not None:
                    self.coords.append([row, col])

    def quit_game(self):
        '''
        Function to save legal moves before quitting.
        Calls on the existing file save function (which uses datetime for unique file names)
        '''
        peg.auto_export_to_file()
        quit()

    def save_game(self):
        '''
        Function to save legal moves; calls on the existing
        file save function (which uses datetime for unique file names)
        '''
        peg.auto_export_to_file()

    def load_moves(self):
        '''Function to open text file, via file browser. Text file loaded into a variable'''
        global pegs_on_board
        self.fname = askopenfilename(filetypes=(("Solution Files", "*.txt"), ("All files", "*.*")))
        if self.fname != '':
            file_contents = open(self.fname)
            data = file_contents.read()
            file_contents.close()
            user_loaded_moves = data.strip().split(',')
            imported_move_count = len(user_loaded_moves)

            # Cycle though the loaded moves
            for user_loaded_move in user_loaded_moves:
                if len(user_loaded_move) == 2:
                    # Extracting origin
                    try:
                        self.user_org_coords = peg_pos_dict[user_loaded_move[0]]
                        # Extracting destination
                        self.user_dest_coords = peg_pos_dict[user_loaded_move[1]]

                        # Ensuring origin and middle are filled and destination are empty.
                        move_direction = peg.validated_middle_peg(self.user_org_coords, self.user_dest_coords)[1]

                        if board_.is_origin_filled(self.user_org_coords, board_.board) \
                                and board_.is_destination_empty(self.user_dest_coords, board_.board) \
                                and board_.is_middle_filled(self.user_org_coords, board_.board, move_direction):

                            # Need to validate each loaded move
                            # Origin and Destination characters must be peg position dictionary
                            if peg.validated_middle_peg(self.user_org_coords, self.user_dest_coords)[0]:
                                # Update the board as per the legal move
                                peg.update_board_pegs(self.user_org_coords,
                                                      peg.validated_middle_peg(self.user_org_coords, self.user_dest_coords)[1],
                                                      self.user_dest_coords, board_.board)

                                # Appending legal move to list
                                peg.add_move(user_loaded_move[0], user_loaded_move[1])

                                # Updating pegs on board up to reflect legal move
                                pegs_on_board -= 1
                                self.create_widgets()
                                root.display_label()

                    except:
                        self.load_error_count += 1
                else:
                    self.load_error_count += 1

            if pegs_on_board == 1:
                tk.messagebox.showinfo(title="Winner!", message="Great Scott - you've done it! Well done!")
            else:
                tk.messagebox.showinfo(title="Import Complete",
                                       message="This import contained {} moves: {} pegs ".format(imported_move_count,
                                                                                                 pegs_on_board)
                                               + "remain and there were {} error(s)".format(self.load_error_count))
            # resetting after warning box is displayed
            load_error_count = 0

    def create_widgets(self):
        '''Function to create all colour coded buttons (i.e. pegs/ holes)'''
        self.chars_copy = self.chars.copy()
        for c in self.coords:
            button_letter = self.chars_copy.pop(0)
            board_viz = {None: ' ', True: 'red', False: 'white'}
            hole_description = board_.board[c[0]][c[1]]
            button_colour =  board_viz[hole_description]

            tk.Button(self,
                      text=button_letter,
                      height = 2,
                      width = 4,
                      font='sans 10 bold',
                      bg = button_colour,
                      command=lambda button_entry_coords = c : set_coords(button_entry_coords, state_of_play)
                      ).grid(row=c[0], column=c[1])

        tk.Button(self, text="Load", command=self.load_moves).grid(row=7, column=2)
        tk.Button(self, text="Save", command=peg.auto_export_to_file).grid(row=7, column=3)
        tk.Button(self, text="Quit", command=self.quit_game).grid(row=7, column=4)

def set_coords(coords, state_of_play_input):
    '''Function to capture the coords and their identity i.e. origin or destination'''
    global org_coords_input
    global dest_coords_input
    global state_of_play

    if state_of_play_input == 0:
        org_coords_input = coords
        state_of_play = 1

    elif state_of_play_input == 1:
        dest_coords_input = coords
        game_play(org_coords_input, dest_coords_input)
        state_of_play = 0


def game_play(org_coords, dest_coords):
    '''The purpose of this function is to call all of the functions created for the text game to:
    1 assess if a legal move has been put forward
    2 determine the direction of travel
    3 update the board if everything is in order'''
    global state_of_play
    global pegs_on_board
    global peg_pos_dict

    org_char = list(peg_pos_dict.keys())[list(peg_pos_dict.values()).index(org_coords)]
    dest_char = list(peg_pos_dict.keys())[list(peg_pos_dict.values()).index(dest_coords)]

    if not peg.validated_middle_peg(org_coords, dest_coords)[0]:
        state_of_play = 0
        tk.messagebox.showinfo(title="Player Information",
                               message="Not a valid move. Select your next origin peg")

    elif peg.validated_middle_peg(org_coords, dest_coords)[0]:
        # Get direction of travel (origin to destination)
        move_direction = peg.validated_middle_peg(org_coords, dest_coords)[1]

        if board_.is_middle_filled(org_coords, board_.board, move_direction) \
                and board_.is_destination_empty(dest_coords, board_.board) \
                and board_.is_origin_filled(org_coords, board_.board):

            peg.update_board_pegs(org_coords, move_direction, dest_coords, board_.board)
            peg.add_move(org_char, dest_char)
            pegs_on_board -= 1
            state_of_play = 0
            root.display_label()

            root.create_widgets()
            if pegs_on_board == 1:
                tk.messagebox.showinfo(title="Winner!", message="Great Scott - you've done it! Well done!")
                peg.auto_export_to_file()


root = tk.Tk()
root.title("Peg Solitaire")
root.geometry("295x365")
root = Application(root)
root.mainloop()