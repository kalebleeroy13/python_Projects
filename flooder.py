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
HEART       = chr(9829) # character 9829 is '♥'.
DIAMOND     = chr(9830) # character 9830 is '♦'.
SPADE       = chr(9824) # character 9824 is '♠'.
CLUB        = chr(9827) # character 9827 is '♣'.
BALL        = chr(9679) # character 9879 is '●'.
TRIANGLE    = chr(9650) # character 9650 is '▲'.

BLOCK       = chr(9608) # character 9608 is '█'
LEFTRIGHT   = chr(9472) # character 9472 is '─'
UPDOWN      = chr(9474) # character 9474 is '│'
DOWNRIGHT   = chr(9484) # character 9484 is '┌'
DOWNLEFT    = chr(9488) # character 9488 is '┐'
UPRIGHT     = chr(9492) # character 9492 is '└'
UPLEFT      = chr (9496) # character 9496 is '┘'
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
    
    print('Do you want to play in colorblind mode Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE

    gameBoard = getNewBoard()
    movesLeft = MOVES_PER_GAME


    while True: # Main game loop.
        displayBoard(gameBoard, displayMode)

        print('Moves left:', movesLeft)
        playerMove = askforPlayerMove(displayMode)
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard, displayMode)
            print('You have run out of moves!')
            break


def getNewBoard():
    """Return a dictionary of a new Flood it board."""

    # Keys are (x, y) tuples, values are the tile at that position.
    board ={}

    # Create random colors for the board.
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x,y)] = random.choice(TILE_TYPES)

    # Make several tiles the same as their neighbor. This creates groups
    # of the same color/shape.
    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_HEIGHT - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x +1,y )] = board[(x,y)]
    return board


