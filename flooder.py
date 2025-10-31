import random, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
BOARD_WIDTH = 16 # (!) Try changing 4 or 40
BOARD_HEIGHT = 14 # (!) Try changin this to 4 or 20
MOVES_PER_GAME = 20 # (!) Try changinthis to 3 or 300

# constant for the diferent shapes used in colorblind mode:
HEART       = chr(9829) 
DIAMOND     = chr(9830)
SPADE       = chr(9824)
CLUB        = chr(9827)
BALL        = chr(9679)
TRIANGLE    = chr(9650)

BLOCK       = chr(9608)
LEFTRIGHT   = chr(9472)
UPDOWN      = chr(9474)
DOWNRIGHT   = chr(9484)
DOWNLEFT    = chr(9488)
UPRIGHT     = chr(9492)
UPLEFT      = chr (9496)
# A list of chr() coes is at https://inventwithpython.com/chr

# All the color/shape tiles used on the board:
tile_types = (0, 1, 2, 3 , 4, 5)

COLORS_MAP = {0: 'red', 1: 'green', 2:'blue',
              3:'yellow', 4:'cyan', 5:'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2:DIAMOND, 
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'

def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Flooder, by Al sweigart al@inventwithpython.com
          
Set the upper left color/shape, which fills in all the 
adjacent squares of that color/shape. Try to make the
entire board the same color/shape.''')

