import random, shutil, sys, time

# constants:
Pause = 0.2 #(!) Try changing this to 1.0 or 0.0
Density = 0.10 # (!)Try changin this to anything from 0.0 to 1.0

DUCKLING_WIDTH = 5 
LEFT ='left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHubby = 'chubby'
Very_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

# find terminal window size:
WIDTH = shutil.get_terminal_size()[0]
# We can't print to the last column on windows without it adding a 
# newline

