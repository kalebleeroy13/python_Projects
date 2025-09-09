"""An art program that draws a continuous line around the screen using the
WASD keys. Inspired by Etch A Sketch toys.

Try drawing a Hilbert Curve fractal with:
RUN SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

Larger hilbert curv fractal with:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD

"""

import shutil, sys

# ─── Line Characters ────────────────────────────────────────────────────────────
UP_DOWN_CHAR            = chr(9474)  # │
LEFT_RIGHT_CHAR         = chr(9472)  # ─
DOWN_RIGHT_CHAR         = chr(9484)  # ┌
DOWN_LEFT_CHAR          = chr(9488)  # ┐
UP_RIGHT_CHAR           = chr(9492)  # └
UP_LEFT_CHAR            = chr(9496)  # ┘
UP_DOWN_RIGHT_CHAR      = chr(9500)  # ├
UP_DOWN_LEFT_CHAR       = chr(9508)  # ┤
DOWN_LEFT_RIGHT_CHAR    = chr(9516)  # ┬
UP_LEFT_RIGHT_CHAR      = chr(9524)  # ┴
CROSS_CHAR              = chr(9532)  # ┼

REVERSE_DIRECTION = {'W': 'S', 'S': 'W', 'A': 'D', 'D': 'A'}

#using frozenset([]): as a dictionary key for mapping direction sets to characters
LINE_CHARS = {
    frozenset(['W', 'S']): UP_DOWN_CHAR,
    frozenset(['A', 'D']): LEFT_RIGHT_CHAR,
    frozenset(['S', 'D']): DOWN_RIGHT_CHAR,
    frozenset(['A', 'S']): DOWN_LEFT_CHAR,
    frozenset(['W', 'D']): UP_RIGHT_CHAR,
    frozenset(['W', 'A']): UP_LEFT_CHAR,
    frozenset(['W', 'S', 'D']): UP_DOWN_RIGHT_CHAR,
    frozenset(['W', 'S', 'A']): UP_DOWN_LEFT_CHAR,
    frozenset(['A', 'S', 'D']): DOWN_LEFT_RIGHT_CHAR,
    frozenset(['W', 'A', 'D']): UP_LEFT_RIGHT_CHAR,
    frozenset(['W', 'A', 'S', 'D']): CROSS_CHAR,
}

# ─── Canvas Setup ───────────────────────────────────────────────────────────────
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5

canvas = {}
cursorX = 0
cursorY = 0
moves = []

# ─── Drawing Logic ──────────────────────────────────────────────────────────────
def getCanvasString(canvasData, cx, cy):
    canvasStr = ''
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
            else:
                cell = canvasData.get((columnNum, rowNum))
                canvasStr += LINE_CHARS.get(frozenset(cell) if cell else frozenset(), ' ')
        canvasStr += '\n'
    return canvasStr

def moveCursor(command):
    global cursorX, cursorY
    if command not in REVERSE_DIRECTION:
        return
    moves.append(command)

    if not canvas:
        canvas[(cursorX, cursorY)] = {command, REVERSE_DIRECTION[command]}

    canvas[(cursorX, cursorY)].add(command)

    if command == 'W' and cursorY > 0:
        cursorY -= 1
    elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
        cursorY += 1
    elif command == 'A' and cursorX > 0:
        cursorX -= 1
    elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
        cursorX += 1
    else:
        return

    canvas.setdefault((cursorX, cursorY), set()).add(REVERSE_DIRECTION[command])

# ─── Main Loop ──────────────────────────────────────────────────────────────────
while True:
    print(getCanvasString(canvas, cursorX, cursorY))
    print('WASD to move, H for help, C to clear, F to save, RUN <moves>, or QUIT.')
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    elif response == 'H':
        print('Use W, A, S, D to move and draw. Example: DDD draws right.')
        print('Use RUN followed by a string to auto-draw. Example:')
        print('RUN SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW')
        print('Use F to save your drawing to a file.')
        input('Press Enter to continue...')
        continue

    elif response == 'C':
        canvas = {}
        moves.append('C')

    elif response == 'F':
        try:
            print('Enter filename to save:')
            filename = input('> ')
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))
        except Exception as e:
            print(f'ERROR: Could not save file. {e}')

    elif response.startswith('RUN '):
        for command in response[4:]:
            moveCursor(command)
        continue

    else:
        for command in response:
            moveCursor(command)
