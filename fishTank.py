import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instruction at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up constants:
WIDTH, HEIGHT = bext.size()
# Can't print to the last column on Windows without it adding a 
# newline automatically, so reduxe the width by one:
WIDTH -= 1

NUM_KELP = 2 # (!) TRY CHANGING THIS TO 10.
NUM_FISH = 10 # (!) TRY changing this to 2 or 100
NUM_BUBBLERS = 1 # (!) Try changing this to 0 or 10.
FRAMES_PER_SECOND = 4 # (!) try changing this number to 1 or 60.
# (!) try changing the constants to create a fish tank with only kelp.
# or only bubblers.

# NOTE: Every string in a dfish dictionary should be the same length.
FISH_TYPES = [
    {'right': ['><>'],          'left': ['<><']},
    {'right': ['>||>'],         'left': ['<||<']},
    {'right': ['))'],           'left': ['<[[<']},
    {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
    {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
    {'right': ['>-==>'],        'left': ['<==-<']},
    {'right': [r'>\\>'],        'left': ['<//<']},
    {'right': ['><)))*>'],      'left': ['<*(((><']},
    {'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
    {'right': [']-<)))b>'],     'left': ['<d(((<-[']},
    {'right': ['><XXX*>'],      'left': ['<*XXX><']},
    {'right': ['_.-._.-^=>', '.-._.-.^=>', 
               '-._.-._^=>', '._.-._.^=>'],
     'left': ['<=^-._.-._', '<=^.-._.-.', 
              '<=^_.-._.-', '<=^._.-._.']},
]