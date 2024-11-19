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