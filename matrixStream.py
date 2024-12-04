import random, shutil, sys, time

# Set up the constansts:
MIN_STREAM_LENGTH = 6 # min distance
MAX_STREAM_LENGTH = 20 # max distance
PAUSE = 0.1 # changes speed of stream
STREAM_CHARS = ['0', '1'] # characters of the stream

# Density can range from 0.0 to 1.0
DENSITY = 0.02 # (!) try changing this to 0.10 or 0.30

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]


print('Matrix Stream')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    # For each column, when the counter is 0, no stream is shown
    # Otherwise, it acts as a counter for how many times a 1 or 0 
    # should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # Set up the counter for each column:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Restart a stream on this column.
                    columns[i] = random.randint(MIN_STREAM_LENGTH, 
                                                MAX_STREAM_LENGTH)

            # Display an empty space or a 1/0 character.
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')

        print() #print a newline at the end of the row of columns.
        sys.stdout.flush() # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is hit , end program