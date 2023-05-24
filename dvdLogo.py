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