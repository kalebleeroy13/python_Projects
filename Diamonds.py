def main():
    print('Rectangle pattern')

    # Display rectangles of different sizes:
    for width, height in [(6, 3), (10, 4), (12, 5)]:
        displayOutLineRectangle(width, height)
        print() # Prints newline
        displayFilledRectangle(width, height)
        print() # Prints newline


def displayOutLineRectangle(width, height): 
    # displays the top half of rectangle:
    print('+' + '-' * (width - 2) + '+')

    # Display sides of rectangle:
    for _ in range(height -2):
        print('|' + ' ' * (width - 2) + '|')

    # Display bottom of rectangle
    print('+' + '-' * (width - 2) + '+')
        
def displayFilledRectangle(width, height):
    # Display filled rectangles:
    for _ in range(height):
        print('#' * width)

# if this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()