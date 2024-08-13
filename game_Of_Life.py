"""Conway's Game of Life, by Al Sweigart al@inventwithpython.com
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wilkipedia.org/wiki/conway%27s_Game_of_Life
View this code at  https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, simulation"""

import copy, random, sys, time

# set up the consants:
WIDTH = 79 # The width of the cell grid. 
HEIGHT = 20 # The height of the cell grid. 

#(!) Try changing Alive to '#' or nother character:
Alive = '0' # The chracter representing a living cell.
#(!) Try changing DEAD to '.' or another character:
DEAD = ' '  # The character representing a dead cell

# (!) Try changin Alice to '|' and DEAD to '-'.

# The cells and nextCells are dictionareis for the state of the game. 
# Their keys are (x,y)tup;es and their values are one of the Alive 
# or DEAD values
nextCells = {}
# Put random dead and alive cells into nextCells:
for x in range(WIDTH): # Loop over every possible column.
    for y in range(HEIGHT): # Loop over every possible row.
        # 50/50 chance for starting cells being alive or dead.
        if random.radint(0,1) == 0:
            nextCells[(x,y)] = Alive # Add a living cell.
        else:
            nextCells[(x,y)] = Dead # Add a dead cell.