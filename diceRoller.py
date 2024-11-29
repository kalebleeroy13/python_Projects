import random
import sys

print('''Dungeon & Dragons dice roller

Enter what kind and how many dice to roll. The format is the number of
dice, followed by the "d", followed by the number of sides the dice have.
You can also add a plus, minus, or multiplication adjustment, and an
option to remove the lowest die roll.

Ex:
    3d6 rolls three 6-sided dice
    1d10+2 rolls one 10-sided die, and adds 2
    2d38-1 rolls two 38-sided dice, and subtracts 1
    2d20*2 rolls two 20-sided dice, and multiplies the result by 2
    4d6-r rolls four 6-sided dice, and removes the lowest roll
    QUIT quits the program
''')

while True:  # Main program loop:
    try:
        diceStr = input('> ')  # Prompt to enter the dice string

        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Clean up the dice string:
        diceStr = diceStr.lower().replace(' ', '')

        # Check if we need to remove the lowest roll
        removeLowest = False
        if '-r' in diceStr:
            removeLowest = True
            diceStr = diceStr.replace('-r', '')

        # Find the "d" in the dice string input:
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        # Get the number of dice. (The "3" in "3d6+1"):
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # Find if there is a plus, minus, or multiplication sign for a modifier:
        plusIndex = diceStr.find('+')
        minusIndex = diceStr.find('-')
        multiplyIndex = diceStr.find('*')
        modIndex = max(plusIndex, minusIndex, multiplyIndex)

        # Find the number of sides. (The "6" in "3d6+1"):
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1:]
        else:
            numberOfSides = diceStr[dIndex + 1:modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)

        # Find the modifier amount. (The "1" in "3d6+1"):
        if modIndex == -1:
            modAmount = 0
            modOperator = None
        else:
            modAmount = int(diceStr[modIndex + 1:])
            modOperator = diceStr[modIndex]

        # Simulate the dice rolls:
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        # Remove the lowest roll if needed:
        if removeLowest:
            print(f'Removing the lowest roll: {min(rolls)}')
            rolls.remove(min(rolls))

        # Calculate the total:
        total = sum(rolls)
        if modOperator == '+':
            total += modAmount
        elif modOperator == '-':
            total -= modAmount
        elif modOperator == '*':
            total *= modAmount

        # Display the total:
        print('Total:', total, '(Each die:', end=' ')

        # Display the individual rolls:
        print(', '.join(map(str, rolls)), end='')

        # Display the modifier amount:
        if modAmount != 0:
            print(', {}{}'.format(modOperator, abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        # Catch any exceptions and display the message to the user:
        print('Invalid input. Enter something like "3d6" or ')
        print('Input was invalid because: ' + str(exc))
        continue  # Go back to the dice string prompt.
