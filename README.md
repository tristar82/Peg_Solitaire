<img src="https://cdn.freelogovectors.net/wp-content/uploads/2020/01/university-of-exeter-logo.png" alt="Univeristy of Exeter Logo" width="100"/>

# HPDM139 Assignment 1 - Peg Solitaire
*Elliott Coyne*

*MSc Health Data Science 2021/2 Cohort*

## Content
- [Assignment Description](#assignment-description)
- [Additional Libraries Used](#additional-libraries-used)
- [Links](#links)

## Assignment Description
The purpose of this assignment was to create a functioning game of Peg Solitaire. The game needed to meet the following requirements:
* allows a user to play the game of peg solitaire via a basic interface;
* allows only the legal moves from peg solitaire;
* allows a user to input moves step by step by loading a solution file that contains a chain of moves; and
* logs the users moves and outputs the log to file.

## Game Operation
Once loaded, the game will ask the player to determine what they would like to do. The options are to Load a (S)oltion File, (P)lay the Game, Read the (R)ules or (E)xit.
The aim of the game is to be lest with just 1 peg in the board.
If loading a partial solution file, the computer will make all the loaded moves before handing over to the player.
Upon exiting the game (after game play), a text file containing all legal moves will by generated and autosaved using the date time to create a unique file name.
If playing the game, the following criteria must be satisfied for a move to be considered legal:
* ORIGIN and MIDDLE peg must be filled;
* DESTINATION hole must be empty; and
* ORIGIN and DESTINATION must be 2 holes (horizotally or vertically) away from eachother; and

## Additional Libraries Used
The Rich Table library was used for enhanced display of the board and character map positions. More details can be found within the [documentation](https://rich.readthedocs.io/en/stable/introduction.html).

## Links
Please find all relevant links for this project below:

- [Github Repository](https://github.com/tristar82/Peg_Solitaire)\
- [Rich Documentation](https://rich.readthedocs.io/en/stable/introduction.html)