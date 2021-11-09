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

while not game_started:
	user_selection_start = menu.initiate_game()

	# Given there are 4 menu options, we'll address each one in turn

	# Load (S)olution File
	if user_selection_start == 'S':
		user_loaded_moves = peg.import_from_file()

		# Cycle though the loaded moves
		for user_loaded_move in user_loaded_moves:
			if len(user_loaded_move) == 2:
				# Extract the origin peg
				try:
					user_org_coords = peg_pos_dict[user_loaded_move[0]]
				except:
					print("The ORIGIN {} ".format(user_loaded_move[0])
						+ "isn't in the peg position dict")

				# Extract the destination peg
				try:
					user_dest_coords = peg_pos_dict[user_loaded_move[1]]
				except:
					print("The DESTINATION {} ".format(user_loaded_move[1])
						+ "isn't in the peg position dict")

				# Need to validate each loaded move
				# Origin and Destination characters must be peg position dictionary
				if peg.validated_middle_peg(user_org_coords, user_dest_coords)[0]:

					# Update the board as per the legal move
					peg.update_board_pegs(user_org_coords,
						peg.validated_middle_peg(user_org_coords, user_dest_coords)[1],
										  user_dest_coords, board_.board)

					# Appending legal move to list
					peg.add_move(user_loaded_move[0], user_loaded_move[1])

					# Updating pegs on board up to reflect legal move
					pegs_on_board -= 1
					varX = 0
					for row in board_.board:
					 	varX += row.count(True)
					print("{} pegs and {} TRUEs".format(varX, pegs_on_board))

				else:
					print("{} doesn't appear to be legal move".format(user_loaded_move))
			else:
				print("Invalid move '{}': expected".format(user_loaded_move)
					  + " input, for example, 'ox'")

		print("\nAfter loading the solution file there are"
				+ " now {} peg(s) on the board\n".format(pegs_on_board))

		if pegs_on_board == 1:
			print("Well done - mission accomplished, you've done it!")
			break
		else:
			game_started = True

	# Display (R)ules
	elif user_selection_start == 'R':
		menu.rules()

	# (E)xit
	elif user_selection_start == 'E':
		quit()

	# (P)lay
	else:
		game_started = True

# Game Started
while pegs_on_board > 1:

	board_.print_map(peg_pos_dict)
	board_.print_board(pegs_on_board)
	print("There are {} pegs remaining on the board".format(pegs_on_board))

	# Setting dummy coordinates, ready to validate user entry moves
	org_coords = [9, 9]
	dest_coords = [9, 9]

	while not peg.validated_middle_peg(org_coords, dest_coords)[0]:

		valid_user_selection = False
		while not valid_user_selection:
			raw_move_chars = input("Please enter your move (or EXIT to quit): ")
			if len(raw_move_chars) == 2:
				org_coords, org_char = peg.verify_input_char(raw_move_chars[0],
						peg_pos_dict, 'origin')
				dest_coords, dest_char = peg.verify_input_char(raw_move_chars[1],
						peg_pos_dict, 'destination')
				valid_user_selection = True
			elif raw_move_chars.upper() == "EXIT":
				peg.auto_export_to_file()
				quit()
			else:
				print("Selection doesn't look right. Please try again. ")

	# Get direction of travel (origin to destination)
	move_direction = peg.validated_middle_peg(org_coords, dest_coords)[1]

	if board_.is_middle_filled(org_coords, board_.board, move_direction) \
		and board_.is_destination_empty(dest_coords, board_.board) \
		and board_.is_origin_filled(org_coords, board_.board):

		# Update the board as per the legal move
		peg.update_board_pegs(org_coords, move_direction, dest_coords, board_.board)

		# Appending legal move to list
		peg.add_move(org_char, dest_char)

		# Updating pegs on board up to reflect legal move
		pegs_on_board -= 1

		print('Nice! Move successful\n')

	else:
		print("Are ORIGIN and MIDDLE holes filled and DESTINATION empty?")


peg.auto_export_to_file()
