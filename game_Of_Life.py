"""Conway's Game of Life, by Al Sweigart al@inventwithpython.com
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wilkipedia.org/wiki/conway%27s_Game_of_Life
View this code at  https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, simulation"""

import copy
import random
import sys
import time

# Set up the constants
WIDTH = 70  # The width of the cell grid
HEIGHT = 20  # The height of the cell grid
ALIVE = '1'  # Character representing a living cell
DEAD = '0'   # Character representing a dead cell

def read_initial_state(file_path):
    """Load initial state from a text file."""
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
        return grid

def print_grid(grid):
    """Print the grid to the console."""
    for row in grid:
        print(''.join(row))

def edit_grid(grid):
    """Allow the user to toggle cells in the grid."""
    while True:
        print_grid(grid)
        print("Enter the cell to toggle (row col) or 'done' to finish:")
        user_input = input().strip()
        if user_input.lower() == 'done':
            break
        try:
            row, col = map(int, user_input.split())
            grid[row][col] = ALIVE if grid[row][col] == DEAD else DEAD
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column numbers.")

def get_neighbors(x, y, width, height):
    """Get the coordinates of the neighbors of a cell."""
    left = (x - 1) % width
    right = (x + 1) % width
    above = (y - 1) % height
    below = (y + 1) % height
    return [(left, above), (x, above), (right, above),
            (left, y), (right, y),
            (left, below), (x, below), (right, below)]

def update_grid(grid):
    """Update the grid according to Conway's Game of Life rules."""
    new_grid = copy.deepcopy(grid)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            alive_neighbors = sum(1 for nx, ny in get_neighbors(x, y, WIDTH, HEIGHT) if grid[ny][nx] == ALIVE)
            if grid[y][x] == ALIVE:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[y][x] = DEAD
            else:
                if alive_neighbors == 3:
                    new_grid[y][x] = ALIVE
    return new_grid

# Initialize the grid
try:
    grid = read_initial_state('initial_state.txt')
except FileNotFoundError:
    print("File not found. Initializing with random states.")
    grid = [[ALIVE if random.random() < 0.5 else DEAD for _ in range(WIDTH)] for _ in range(HEIGHT)]

edit_grid(grid)

while True:
    print('\n' * 50)  # Clear the screen
    print_grid(grid)   # Display the current grid
    grid = update_grid(grid)  # Update the grid for the next generation
    time.sleep(1)  # Pause for visualization

    try:
        time.sleep(1) #Add a 1 second pause to reduce flickering.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print('by Al sweigart al@inventwithpython.com')
        sys.exit() #when Ctrl-C is pressed, end the program.