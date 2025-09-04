"""An art program that draws a continuos line around the screen using the
WASD keys. Inspired by Etch A Sketch toys.

For example, you can draw Hilbert Curve fractal with:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

 larger Hilbert Curve fractal with:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD"""

import shutil, sys

# Set ip the constants for the line chatacters:
UP_DOWN_CHAR            = chr(9474) # Character 9474 is '|'
LEFT_RIGHT_CHAR         = chr(9472) # Character 9472 is '-'
DOWN_RIGHT_CHAR         = chr(9484) # Character 9484 is '┌'
DOWN_LEFT_CHAR          = chr(9488) # Character 9488 is '┐'
UP_RIGHT_CHAR           = chr(9492) # Character 9492 is '└'
UP_LEFT_CHAR            = chr(9496) # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR      = chr(9500) # Character 9500 is '├'
UP_DOWN_LEFT_CHAR       = chr(9508) # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR    = chr(9516) # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR      = chr(9524) # Character 9524 is '┴'
CROSS_CHAR              = chr(9532) # Character 9532 is '┼'
# A list of chr() codes is at hhtps:inventwithpython.com/chr

# Get the size of the terminal window:
CANVAS_WIDTH, CANVAS_HEIGHT =shutil.get_terminal_size()
# We can't print to the last column on Window withouth it adding a 
# newline automaitcally, so reduve the width by one:
CANVAS_WIDTH -= 1
# leave room at the bottom few rows for the command info lines. 
CANVAS_HEIGHT -= 5

""" The keys for canvas willl be (x, y) interger tuples for the coordinate,
and the value is a set of letterss W, A, S, D that tell what kind of line
 should be drawn."""
canvas = {}
cursorX = 0 
cursorY = 0


def getCanvasString(canvasData, cx, cy):
    """Rturns a multiline string of line drawn in canvasData."""
    canvasStr = ''

    """canvasData is a dictionary with (x,y) tuple keys and values that
    are sets of 'W', 'A', 'S', and/or 'D' strings to show which 
    directions the lines are drawn at each xy point."""
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue
            # Add the line character for this point to canvasStr.
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell in (set(['S', 'D']), set(['A']), set(['D'])):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell in (set(['A', 'S']), set(['A']), set(['D'])):
                canvasStr += DOWN_LEFT_CHAR
            elif cell in (set(['W', 'D']), set(['A']), set(['D'])):
                canvasStr += UP_RIGHT_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += UP_LEFT_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
