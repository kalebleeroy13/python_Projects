import random, time

# setup constants
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3 # -3 for room to enter the sum at the bottom.

# duration in seconds:
QUIZ_DURATION = 30 # (!) TRY CHANGING TO 10 OR 60
MIN_DICE = 2 # (!) TRY CHANGING TO 1 OR 5 
MAX_DICE = 6 # (!) TRY CHANGING THIS TO 14

# (!) CHANGE TO DIFFERENT NUMBER
REWARD = 4 # (!) points awarded for correct answers.
PENALTY = 1 # (!) POINTS REMOCED FOR INCORRECR ANSWERS.
# (!) TRY SETTING PENALTY TO A NEGATIVE NUUMBER TO GIVE POINTS FOR WRONG ANSWERS

# The program hangs if all of the dice can't fit on the screen:
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   0   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| 0     |',
        '|       |',
        '|     0 |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     0 |',
        '|       |',
        '| 0     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| 0     |',
        '|   0   |',
        '|     0 |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     0 |',
        '|   0   |',
        '| 0     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| 0   0 |',
       '|       |',
       '| 0   0 |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| 0   0 |',
       '|   0   |',
       '| 0   0 |',
       '+-------+'], 5)

D6 = (['+-------+',
       '| 0   0 |',
       '| 0   0 |',
       '| 0   0 |',
       '+-------+'], 6)

D6b = (['+-------+',
        '| 0 0 0 |',
        '|       |',
        '| 0 0 0 |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3b, D4, D5, D6a, D6b]

print('''Dice Math
Add up the sides of all the dice displayed on the screen. 
You have {} seconds to answer as many as possible. You get {} points for each
correct answer and lose {} points for each incorrect answer.'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press enter to begin...')

# Keep track of how many answers were correct and incorrrect:
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION: # main loop.
    # come up with the dice to display:
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        # die[0] contains the list of strings of the die face:
        diceFaces.append(die[0])
        # die[1] contains the intedger number of pips on the face:
        sumAnswer += die[1]
    
    # Contains (x,y) tuples of the top-left corner of each die. 
    topLeftDiceCorners = []

    # Figure out where dice should go:
    for i in range(len(diceFaces)):
        while True:
            # Find a random place on the canvas to put the die. 
            left = random.randit(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randit(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # Get the x, y coordinates for all four corners:
            #   left
            #   v
            #top > +-------+ ^,
            #      | 0     |,
            #      |   0   |,   DICE_HEIGHT(5)
            #      |     0 |,   |
            #      +-------+    v
            #      DICE_WIDTH (9)
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT


            # Check if this die overlaps with dice. 
            overlaps = False 
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT
                # Check each corner of this die to see if it is insede
                # of the area the previous die:
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY)
                                         (bottomLeftX, bottomRightY)
                                         (bottomRightX, bottomLeftY)):
                    if(prevDieLeft <= cornerX < prevDieRight
                        and prevDieTop <= cornerY < prevDieBottom):
                            overlaps = True
            if not overlaps:
                # it doesn't overlap, so we can put it here:
                topLeftDiceCorners.append((left, top))
                break

    # Draw the dice on the canvas:

    # Keys are (x, y) tuples of ints, values the character at that
    # position on the canvas:
    canvas = {}
    # Loop over each die:
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        # Loop over each character in the die's face:
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # copy this character to the correct place on the canvas:
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                # Note that in dieFace, a list of strings, the x and y 
                # are swapped:
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    # Display the canvas on the screen:
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
            print() # Print a newline
        
        # Let the player enter their answer:
        response = input('Enter the sum: ').strip()
        if response.isdecimal() and int(response) == sumAnswer:
            correctAnswers += 1
        else:
            print('Incorrect, the anwer is', sumAnswer)
            time.sleep(2)
            incorrectAnswers += 1

# Display the final score:
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct: ', correctAnswers)
print('Incorrect:', incorrectAnswers)
print('Score  ', score)
