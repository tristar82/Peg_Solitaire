# GUI Version of the Peg Solitaire Assignment - Advanced Section

import tkinter as tk
import os
import datetime

####### start of import from Text Game
from peg_solitaire import Board
from peg_solitaire import Peg
from peg_solitaire import Menu

menu = Menu()
peg = Peg()
board_ = Board()

game_started = False
pegs_on_board = 32
peg_pos_dict = board_.peg_pos_dict
####### end of import from Text Game

global state_of_play  # can remove if commenting out the bottom line below.
global org_coords_input
global dest_coords_input

state_of_play = 0
org_coords_input = None
dest_coords_input = None


class Application(tk.Frame):
    def __init__(self, master):
        """This initializes the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.coords = []
        self.chars_copy = None
        self.base = [chr(i) for i in range(97, 113)]
        self.chars = self.base + ['x'] + [i.upper() for i in self.base[::-1]]

        self.create_grid_coords()
        self.create_widgets()

    def display_label(self):
        tk.Label(text="{} Pegs Remaining".format(pegs_on_board)).grid(row=7, column=0)

    def create_grid_coords(self):
        raw_grid = [[not row == ele == 3 if ele in [2, 3, 4] or row in [2, 3, 4] else None for row in range(7)] for ele
                    in range(7)]
        for row in range(len(raw_grid)):
            for col in range(len(raw_grid[row])):
                if raw_grid[row][col] is not None:
                    self.coords.append([row, col])
        print(raw_grid)

    def create_widgets(self):
        self.chars_copy = self.chars.copy()
        for c in self.coords:
            #self.chars_copy = self.chars.copy()
            button_letter = self.chars_copy.pop(0)
            ####
            board_viz = {None: ' ', True: 'blue', False: 'red'}
            hole_description = board_.board[c[0]][c[1]]
            button_colour =  board_viz[hole_description]
            ####
            tk.Button(self,
                      text=button_letter,
                      height = 2,
                      width = 4,
                      font='sans 10 bold',
                      bg = button_colour,
                      command=lambda button_entry_coords = c : set_coords(button_entry_coords, state_of_play)
                      ).grid(row=c[0], column=c[1])

def set_coords(coords, state_of_play_input):
    '''Function to capture the coords and their identity i.e. origin or destination'''
    # global input_coords
    global org_coords_input
    global dest_coords_input
    global state_of_play  # can remove if commenting out the bottom line below.
    if state_of_play_input == 0:
        org_coords_input = coords
        state_of_play = 1
        print("The origin has been set to {} and the state of play is {}".format(org_coords_input,state_of_play ))
    elif state_of_play_input == 1:
        dest_coords_input = coords
        mega_function(org_coords_input, dest_coords_input)
        print("The destination has been set to {} and the state of play is {}".format(dest_coords_input, state_of_play))
        #state_of_play = 0


########################################### START OF RECYCLED CODE

def mega_function(org_coords, dest_coords):
    '''The purpose of this function is to call all of the functions created for the text game to:
    1 assess if a legal move has been put forward
    2 determine the direction of travel
    3 update the board if everything is in order'''
    global state_of_play
    global pegs_on_board
    global  peg_pos_dict

    org_char = list(peg_pos_dict.keys())[list(peg_pos_dict.values()).index(org_coords)]
    dest_char = list(peg_pos_dict.keys())[list(peg_pos_dict.values()).index(dest_coords)]

    if not peg.validated_middle_peg(org_coords, dest_coords)[0]:
        state_of_play = 0 #
        print("Not a valid move. Select your next origin peg")
    elif peg.validated_middle_peg(org_coords, dest_coords)[0]:
        ## Get direction of travel (origin to destination)
        move_direction = peg.validated_middle_peg(org_coords, dest_coords)[1]

        if board_.is_middle_filled(org_coords, board_.board, move_direction) \
                and board_.is_destination_empty(dest_coords, board_.board) \
                and board_.is_origin_filled(org_coords, board_.board):

            peg.update_board_pegs(org_coords, move_direction, dest_coords, board_.board)
            peg.add_move(org_char, dest_char) # need to look up coords to character
            pegs_on_board -= 1
            state_of_play = 0
            root.display_label()
            print("I think this worked")
            print(pegs_on_board)
            print(board_.board)
            root.create_widgets()
            if pegs_on_board == 1:
                peg.auto_export_to_file()
        else:
            print("Are ORIGIN and MIDDLE holes empty filled and DESTINATION empty?")

########################################### END OF RECYCLED CODE

root = tk.Tk()
root.title("Peg Solitaire")
#root.geometry("350x350")
root = Application(root)
root.mainloop()