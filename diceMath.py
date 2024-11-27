import random, time, sys

# setup constants
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3 for room to enter the sum at the bottom.

# duration in seconds:
QUIZ_DURATION = 30  # (!) TRY CHANGING TO 10 OR 60
MIN_DICE = 2  # (!) TRY CHANGING TO 1 OR 5 
MAX_DICE = 6  # (!) TRY CHANGING THIS TO 14

# (!) CHANGE TO DIFFERENT NUMBER
REWARD = 4  # (!) points awarded for correct answers.
PENALTY = 1  # (!) POINTS REMOVED FOR INCORRECT ANSWERS.
# (!) TRY SETTING PENALTY TO A NEGATIVE NUMBER TO GIVE POINTS FOR WRONG ANSWERS

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

D6a = (['+-------+',
       '| 0   0 |',
       '| 0   0 |',
       '| 0   0 |',
       '+-------+'], 6)

D6b = (['+-------+',
        '| 0 0 0 |',
        '|       |',
        '| 0 0 0 |',
        '+-------+'], 6)

D7a = (['+-------+',
        '| 0 0 0 |',
        '|   0   |',
        '| 0 0 0 |',
        '+-------+'], 7)

D7b = (['+-------+',
        '| 0   0 |',
        '| 0 0 0 |',
        '| 0   0 |',
        '+-------+'], 7)       

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b, D7a, D7b]

print('''Dice Math
Add up the sides of all the dice displayed on the screen. 
You have {} seconds to answer as many as possible. You get {} points for each
correct answer and lose {} points for each incorrect answer.'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press enter to begin...')

#keep track of how many answers were correct and incorrect:
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()

try:
    while time.time() < startTime + QUIZ_DURATION:  # main loop.
        # dice generation
        sumAnswer = 0
        diceFaces = []
        for i in range(random.randint(MIN_DICE, MAX_DICE)):
            die = random.choice(ALL_DICE)
            diceFaces.append(die[0])
            sumAnswer += die[1]
        
        topLeftDiceCorners = []
        
        # Dice placement
        for i in range(len(diceFaces)):
            while True:
                left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
                top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)
                
                topLeftX = left
                topLeftY = top
                topRightX = left + DICE_WIDTH
                topRightY = top
                bottomLeftX = left
                bottomLeftY = top + DICE_HEIGHT
                bottomRightX = left + DICE_WIDTH
                bottomRightY = top + DICE_HEIGHT
                
                # check for overlap between die
                overlaps = False 
                for prevDieLeft, prevDieTop in topLeftDiceCorners:
                    prevDieRight = prevDieLeft + DICE_WIDTH
                    prevDieBottom = prevDieTop + DICE_HEIGHT
                    for cornerX, cornerY in ((topLeftX, topLeftY),
                                             (topRightX, topRightY),
                                             (bottomLeftX, bottomRightY),
                                             (bottomRightX, bottomLeftY)):
                        if(prevDieLeft <= cornerX < prevDieRight
                           and prevDieTop <= cornerY < prevDieBottom):
                                overlaps = True
                if not overlaps:
                    topLeftDiceCorners.append((left, top))
                    break
        


        #loop over die
        canvas = {}
        for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
            dieFace = diceFaces[i]
            for dx in range(DICE_WIDTH):
                for dy in range(DICE_HEIGHT):
                    canvasX = dieLeft + dx
                    canvasY = dieTop + dy
                    canvas[(canvasX, canvasY)] = dieFace[dy][dx]

        # canvas display on-screen
        for cy in range(CANVAS_HEIGHT):
            for cx in range(CANVAS_WIDTH):
                print(canvas.get((cx, cy), ' '), end='')
            print()
        
        # player answer
        response = input('Enter the sum: ').strip()
        if response.isdecimal() and int(response) == sumAnswer:
            correctAnswers += 1
        else:
            print('Incorrect, the answer is', sumAnswer)
            time.sleep(2)
            incorrectAnswers += 1
except KeyboardInterrupt:
    print("\nProcess interrupted. Exiting gracefully.")
    sys.exit()

score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct: ', correctAnswers)
print('Incorrect:', incorrectAnswers)
print('Score: ', score)
