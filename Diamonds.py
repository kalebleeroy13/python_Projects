def main():
    print('Diamond pattern')

    # Display diamonds of sizes 0 through 6:
    for diamondSize in range(0,6):
        displayOutLineDiamond(diamondSize)
        print() # Prints newline
        displayFilledDiamond(diamondSize)
        print() # Prints newline


def displayOutLineDiamond(size): 
    # displays the top half of diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='') # Left side space
        print('/', end='') #left side of diamond.
        print('@' * (i * 2), end='') # diamond interior
        print('\\') # Right side of diamond.

    # Display the bottom half of the diamond:
    for i in range(size):
        print(' ' * i, end='') # Left side space
        print('\\', end='') #left side of diamond. 
        print(' ' * ((size - i - 1) * 2), end='') # Diamond interior
        print('/' ) #Right side of diamond. 

def displayFilledDiamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='') #left side space.
        print('/' * (i + 1), end='') # Left half of diamond. 
        print('\\' * (i + 1)) # Right half of diamond.

    # Display bottom half of diamond:
    for i in range(size):
        print(' ' * i, end='') # Left side space.
        print('\\' * (size - i ), end='') # Left side diamond.
        print('/' * (size - i)) # Right side diamond.

# if this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()