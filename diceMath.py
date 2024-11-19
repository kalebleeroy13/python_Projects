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