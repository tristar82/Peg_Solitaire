<img src="https://cdn.freelogovectors.net/wp-content/uploads/2020/01/university-of-exeter-logo.png" alt="Univeristy of Exeter Logo" width="100"/>

# HPDM139 Assignment 1 - Peg Solitaire
*Elliott Coyne*

*MSc Health Data Science 2021/2 Cohort*

## Content
- [Assignment Description](#assignment-description)
- [Instructions for Use](#[instructionsufor-use)
- [Game Operation](#game-operation)
- [Game Rules](#game-rules)
- [Additional Libraries Used](#additional-libraries-used)
- [Links](#links)

## Assignment Description
The purpose of this assignment was to create a functioning game of Peg Solitaire. The game needed to meet the following requirements:
* allows a user to play the game of peg solitaire via a basic interface;
* allows only the legal moves from peg solitaire;
* allows a user to input moves step by step by loading a solution file that contains a chain of moves; and
* logs the users moves and outputs the log to file.

## Instructions for Use
**Please note the library dependencies as listed below in *Additional Libraries Used***
* To run the TEXT based version of the game, run the ***"main.py"*** in the Python terminal. This will load the menu to faciliate game play. 
* To run the Windows GUI (advanced) version of the game, run the ***"GUI_main.py"*** in the Python terminal. This will launch a new window with buttons for different operations.

**Testing**
* To ensure that both the Text and GUI versions can handle solution import files, please refer to the ***garbage_moves.txt*** and ***garbage_moves2.txt*** files respectively. These = can each be imported and handled correctly.


## Game Operation
#### Text Version
Once loaded, the game will ask the player to determine what they would like to do. The options are to Load a (**S**)oltion File, (**P**)lay the Game, Read the (**R**)ules or (**E**)xit.
After loading a solution file (which is assumed to be in the current working directory), the player can enter the next move of their own choice (provided there are pegs remaining).
Legal moves will be in the format 'ox' or 'ex'.

#### GUI Advanced Version
The game will load and display the board; red buttons indicate pegs and white are holes. Simply click first on the origin then the destination buttons; the computer will assess the move and reduce the peg count (displayed at the bottom of the screen) if successful.

Solution files may be loaded by clicking on the **Load** button, which will open the File Browser. Descriptive feedback will be provided after the file has been loaded and moves considered.

#### Both Versions
The aim of the game is to be left with just 1 peg in the board.

If loading a partial solution file, the computer will make all the loaded moves before handing over to the player. Any subsequent moves will be appended to loaded moves and appear as a single file in the export.

The number of pegs remaining will appear on bottom of the window after the first successful move is made.

Upon exiting the game (after game play), a text file containing all legal moves will by generated and autosaved using the date time to create a unique file name.

If playing the game, the following criteria must be satisfied for a move to be considered legal:
* ORIGIN and MIDDLE peg must be filled;
* DESTINATION hole must be empty; and
* ORIGIN and DESTINATION must be 2 holes (horizotally or vertically) away from eachother; and

## Game Rules
* Peg solitaire is a game for one player. There are 33 holes arranged in a 'plus' symbol configuration. The peg in the centre is removed. This leaves 32 pegs.

* The objective of the game is to end up with one peg in the middle hole. This is achieved by removing one peg at a time by jumping an adjacent peg over it into an adjacent empty hole in the other side."

* For example, the peg marked with a cross would be removed by jumping the peg marked with a triangle into the hole in  the centre (shaded). No diagonal jumps are permitted.

## Additional Libraries Used
* The Rich (v 10.12.0) library was used for enhanced display of the board and character map positions. More details can be found within the [documentation](https://rich.readthedocs.io/en/stable/introduction.html).
* Tkinter (tk v 8.6.10) was used for the GUI version of the application. More details can be found within the [documentation](https://tkdocs.com/).

## Links
Please find all relevant links for this project below:

- [Github Repository](https://github.com/tristar82/Peg_Solitaire) 
- [Rich Documentation](https://rich.readthedocs.io/en/stable/introduction.html)
- [Tk (tkinter) Documentation](https://tkdocs.com/)