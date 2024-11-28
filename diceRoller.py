import random, sys

print(''' Dungeon & Dragons dice roller

Enter what kind and how many dice to roll. the format is the number of
 dice, followed by the "d", followed by the number of sides the dice have.
 You can also add a plus or minus adjustment.
 
 Ex:
    3d6 rolls three 6-sided dice
    1d10+2 rolls one 10 sided die, and adds 2
    2d38-1 rolls two 38 -sided die, and subtract 1
    QUIT quits the program
     ''')

while True: # Main program Loop:
    try:
        diceStr = input('> ') # the prompt to enter the dice string
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Clean up the dice string:
        diceStr = diceStr.lower().replace(' ', '')

        # Find the "d" in the dice string input:
        dIndex == diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        #get the number of dice. (The "3" in "3d6+1"):
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # Find the number of sides. (the "6 in 3d6+1"):
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides
