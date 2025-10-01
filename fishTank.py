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
    ]   # (1) try adding fish to FISH_TYPES.
LONGEST_FISH_LENGTH = 10 # Longest single string in FISH_TYPES.

# The x and y postions where a fish runs into the edge of the screen:
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT -2


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear

    # Generate the global variables:
    FISHES = []
    for i in range(NUM_FISH):
        # Each bubbler starts at a random position.
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments' : []}
        # Generate each segment of the kelp:
        for i in range(random.randint(6, HEIGHT -1)):
            kelp['segements'].append(random.choice(['(',')']))
        KELPS.append(kelp)

    # Run the simulation:
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND) 
        clearAquarium()
        STEP += 1


def getRandomColor():
    """Return a strung of a random color."""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))



def generateFish():
    """Return. dictionary that represents a fish."""
    fishyType = random.choice(FISH_TYPES)

    # Set up colors for each character in the fish text:
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishyType['right'][0])
    if colorPattern == 'random': # All parts are randomly colored.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength # All the same color.
    if colorPattern == 'head-tail' # Head/tail different from body.
        headTailColor = getRandomColor()
        colors[0] = headTailColor # Set head color.
        colors[-1] = headTailColor # set tail color.