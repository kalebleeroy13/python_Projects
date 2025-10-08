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
# newline automatically, so reduce the width by one:
WIDTH -= 1

NUM_CRABS = 3  # NUMBER OF CRABS IN TANK

NUM_KELP = 2 # (!) TRY CHANGING THIS TO 10.
NUM_FISH = 10 # (!) TRY changing this to 2 or 100
NUM_BUBBLERS = 1 # (!) Try changing this to 0 or 10.
FRAMES_PER_SECOND = 4 # (!) try changing this number to 1 or 60.
# (!) try changing the constants to create a fish tank with only kelp.
# or only bubblers.

# NOTE: Every string in a fish dictionary should be the same length.
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

# NOTE crab dictionary
CRAB_TYPES = ['(v)', '<v>', '[v]', '{v}', '<(v)>', '[=v=]']  # You can get creative here!


# The x and y postions where a fish runs into the edge of the screen:
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT -2


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP, CRABS
    bext.bg('black')
    bext.clear()

    # Generate the global variables:
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # NOTE: Bubbles are drawn, but not the bubblers themselves.
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # Each bubbler starts at a random position.
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments' : []}
        # Generate each segment of the kelp:
        for i in range(random.randint(6, HEIGHT -1)):
            kelp['segments'].append(random.choice(['(',')']))
        KELPS.append(kelp)

    # Initialize crabs
    CRABS =[]
    for _ in range(NUM_CRABS):
        crab = {
            'x': random.randint(LEFT_EDGE, WIDTH - 3),
            'y': HEIGHT - 2,
            'text': random.choice(CRAB_TYPES),
            'color': getRandomColor(),
            'direction': random.choice(['left', 'right']),
            'speed' : random.randint(2, 6),
            'timeToChange': random.randint(10, 40)
        }
        CRABS.append(crab)


    # Run the simulation:
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND) 
        clearAquarium()
        STEP += 1


def getRandomColor():
    """Return a string of a random color."""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))



def generateFish():
    """Return a dictionary that represents a fish."""
    fishType = random.choice(FISH_TYPES)

    # Set up colors for each character in the fish text:
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = max(len(s) for s in fishType['right'] + fishType['left'])
    if colorPattern == 'random': # All parts are randomly colored.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength # All the same color.
    if colorPattern == 'head-tail': # Head/tail different from body.
        headTailColor = getRandomColor()
        colors[0] = headTailColor # Set head color.
        colors[-1] = headTailColor # set tail color.

    # Set up the rest of fish data structure:
    fish = {'right':            fishType['right'],
            'left':             fishType['left'],
            'colors':           colors,
            'hSpeed':           random.randint(1, 6),
            'vSpeed':           random.randint(5, 15),
            'timeToHDirChange': random.randint(10, 60),
            'timeToVDirChange': random.randint(2, 20),
            'goingRight':       random.choice([True, False]),
            'goingDown':        random.choice([True, False])}
    
    # 'x' is always the leftmost side of the fish body:
    fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0, HEIGHT - 2)
    return fish


def simulateAquarium():
    """Simulate the movements in the aquarium for one step."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP
    
    # Simulate the fish for one step:
    for fish in FISHES:
        # Move the fish horizontally:
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1 #Move the fish right.
                else:
                    fish['goingRight'] = False # Turn the fish around.
                    fish['colors'].reverse() # turn the colors around
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1 # Mover the fish left.
                else:
                    fish['goingRight'] = True # Turn the fish around.
                    fish['colors'].reverse() # Turn the colors around.

        # fish can randomly change their horizontal direction:
        fish['timeToHDirChange'] -= 1
        if fish['timeToHDirChange'] == 0:
            fish['timeToHDirChange'] = random.randint(10, 60)
            # Turn the fish around:
            fish['goingRight'] = not fish['goingRight']

        # Move the fish verically
        if STEP % fish['vSpeed'] == 0:
            if fish['goingDown']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1 # Move the fish down.
                else:
                    fish['goingDown'] = False # Turn the fish around.
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1 # Move the fish up.
                else:
                    fish['goingDown'] = True # Turn the around.

        # Fish can radomly change their vertical direction:
        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['timeToVDirChange'] =random.randint(2, 20)
            # turn the fish around:
            fish['goingDown'] = not fish['goingDown']

    # 🦀 Simulate crab movement
    for crab in CRABS:
        if STEP % crab['speed'] == 0:
            if crab['direction'] == 'right':
                if crab['x'] < WIDTH - len(crab['text']):
                    crab['x'] += 1
                else:
                    crab['direction'] = 'left'
            else:
                if crab['x'] > LEFT_EDGE:
                    crab['x'] -= 1
                else:
                    crab['direction'] = 'right'

        crab['timeToChange'] -= 1
        if crab['timeToChange'] == 0:
            crab['direction'] = random.choice(['left', 'right'])
            crab['timeToChange'] = random.randint(10, 40)


    # generate bubbles from bubblers:
    for bubbler in BUBBLERS:
        # There is a 1 in 5 chance of making a bubbble:
        if random.randint(1, 5) ==1:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT -2})

    # Move the bubbles:
    for bubble in BUBBLES:
        diceRoll = random.randint(1, 6)
        if(diceRoll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1 # Bubble goes left.
        elif (diceRoll == 2) and (bubble['x'] != RIGHT_EDGE):
            bubble['x'] += 1 # Bubble goes right.

        bubble['y'] -= 1 # the bubble always goes up.

    # Iterate over BUBBLES in revers because I'm deleting from BUBBLES
    # while iterating over it.
    for i in range(len(BUBBLES) -1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE: # Delete bubbles that reach the top.
            del BUBBLES[i]

    # Simulate the kelp waving for one step:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            # 1 in 20 chance to change waving:
            if random.randint(1, 20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('


def drawAquarium():
    """Draw the aquarium on the screen."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP, CRABS

    # Draw quit message.
    bext.fg('white')
    bext.goto(0,0)
    print('fish Tank, by AL Sweigart Ctrl-C to quit.', end='')

    # Draw the bubbles:
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', '0')), end='')

    # Draw the fish:
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # Get the correct right- or left-facing fish txt.
        if fish['goingRight']:
            fishText = fish['right'][STEP % len(fish['right'])]
        else:
            fishText = fish['left'][STEP % len(fish['left'])]
        
        # draw each character of the fish text in the right color.
        for i, fishPart in enumerate(fishText):
            bext.fg(fish['colors'][i])
            print(fishPart, end='')

    # Draw the kelp
    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if kelpSegment == '(':
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            elif kelpSegment == ')':
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i)
            print(kelpSegment, end='')

    # Draw the sand on the bottom:
    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH -1), end='') # Draws sand.

    # 🦀 Draw the crabs
    for crab in CRABS:
        bext.fg(crab['color'])
        bext.goto(crab['x'], crab['y'])
        print(crab['text'], end='')


    sys.stdout.flush() # (Required for bext-using programs.)

def clearAquarium():
    """Draw empty spaces over everything on the screen."""
    global FISHES, BUBBLERS, BUBBLES, KELP, CRABS

    # Draw the bubbles:
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')

    # Draw the fish:
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        # Draw each character of the fish text in the right color.
        print(' ' * len(fish['left'][0]), end='')

    # Draw the kelp:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print(' ', end='')
    
    # 🦀 Clear the crabs
    for crab in CRABS:
        bext.goto(crab['x'], crab['y'])
        print(' ' * len(crab['text']), end='')


    sys.stdout.flush() # (Required for bext-using programs.)


# If this program was run(instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() # When Ctrl-C is pressed, end the program.