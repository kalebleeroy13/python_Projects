""""Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop.

Note Do not resize the terminal window while this program is running. 
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, bext"""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions ar')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT, = bext.size()
# We can't print to the last column on Windows without it adding a 
# newline automatically,so reduce the width by one:
WIDTH -= 1

NUMBER_OF_LOGOS = 5 # (!) Try changing this to 1 or 100
PAUSE_AMOUNT = 0.2 # (!) TRY changing this to 1.0 or 0.0.
# (!) Try changing this list to fewer colors:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT    = 'ur'
UP_LEFT     = 'ul'
DOWN_RIGHT  = 'dr'
DOWN_LEFT   = 'dl'
DIRECTIONS  = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries
COLOR = 'color'
X = 'x'
Y = 'y'
Dir = 'direction'


def main():
    bext.clear()

    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos [-1][X] % 2 == 1:
            # Make sure X is even so it can hit the corner.
            logos[-1][X] -= 1

    cornerBounces = 0 #Count how many times a logo hits a corner.
    while True: # Main program loop.
        for logo in logos: #handle eack logo in the logos list.
            # Erase the logo's current location:
            bext.goto(logo[X], logo[Y])
            print('    ', end='') # (!)Try  commenting this line out.

            originalDirectin = logo[Dir]

            # See if the logo bounces pff the corners:
            if logo[X] == 0 and logo[Y] == 0:
                logo[Dir] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[Dir] = DOWN_LEFT
                cornerbounces += 1
            elif logo[X] == Width - 3 and logo[Y] == Height - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # See if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the right edge:
            #  (WIDTH - 3 because 'DVD' has 3 letters.)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT 
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT 