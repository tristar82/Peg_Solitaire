# Game of Peg Solitaire for HPDM139 Assignment 1
# By Elliott Coyne
# Please refer to readme.md for more details.

# Importing Peg, Board and Menu classes from peg_solitaire.py file

from peg_solitaire import Board
from peg_solitaire import Peg
from peg_solitaire import Menu

menu = Menu()
peg = Peg()
board_ = Board()

game_started = False
pegs_on_board = 32
peg_pos_dict = board_.peg_pos_dict

menu.display_welcome()

while game_started == False:
	user_selection_start = menu.initiate_game()

	# Load Solutions File
	if user_selection_start == 'S':
		load_moves_useable = False
		while  load_moves_useable == False:
			try:
				user_loaded_moves = peg.import_from_file()

				# Cycle though the loaded moves
				for user_loaded_move in user_loaded_moves:
					if len(user_loaded_move) == 2:
						# Extract the origin peg
						user_org_coords = peg_pos_dict[user_loaded_move[0]]
						# Extract the destination peg
						user_dest_coords = peg_pos_dict[user_loaded_move[1]]

						# Update the board as per the legal move
						peg.update_board_pegs(user_org_coords, \
							peg.validated_middle_peg(user_org_coords, user_dest_coords)[1],
											 user_dest_coords, board_.board)
						peg.add_move(user_loaded_move[0], user_loaded_move[1])

						pegs_on_board -= 1

				print("\nAfter loading the solution file, there are now {} peg(s) on the board\n"\
					.format(pegs_on_board))

				if pegs_on_board == 1:
					print("Well done you've done it!")
					quit()
				else:
					game_started = True

				load_moves_useable = True
			except:
				print("There seems to be an issue with the solution file loaded")

	# Display Rules
	elif user_selection_start == 'R':
		menu.rules()

	# Exit
	elif user_selection_start == 'E':
		quit()

	# Play
	else:
		game_started = True

# Game Started
while pegs_on_board > 1:

	board_.print_map(peg_pos_dict)
	board_.print_board(pegs_on_board)
	print("There are {} pegs remaining on the board".format(pegs_on_board))

	# Setting dummy coordinates, ready to validate user entry moves
	org_coords = [9,9]
	dest_coords = [9,9]

	while not peg.validated_middle_peg(org_coords, dest_coords)[0]:

		valid_user_selection = False
		while valid_user_selection == False:
			raw_move_chars = input("Please enter your move (or EXIT to quit): ")
			if len(raw_move_chars) == 2:
				org_coords, org_char = peg.verify_input_char(raw_move_chars[0], \
					peg_pos_dict, 'origin')
				dest_coords, dest_char = peg.verify_input_char(raw_move_chars[1], \
					peg_pos_dict, 'destination')
				valid_user_selection = True
			elif raw_move_chars.upper() == "EXIT":
				peg.auto_export_to_file()
				quit()
			else:
				print("Selection doesn't look right. Please try again. ")

	## Get direction of travel (origin to destination)
	move_direction = peg.validated_middle_peg(org_coords, dest_coords)[1]

	if board_.is_middle_filled(org_coords, board_.board, move_direction) \
			and board_.is_destination_empty(dest_coords, board_.board) \
			and board_.is_origin_filled(org_coords, board_.board):

		peg.update_board_pegs(org_coords, move_direction, dest_coords, board_.board)
		peg.add_move(org_char, dest_char)
		pegs_on_board -= 1

		print('Nice! Move successful\n')

	else:
		print("Are ORIGIN and MIDDLE holes filled and DESTINATION empty?")


peg.auto_export_to_file()