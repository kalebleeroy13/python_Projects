import random, shutil, sys, time

# Set up the constanst:
MIN_STREAM_LENGTH = 6 #(!) Try changing this to 1 or 50.
MAX_STREAM_LENGTH = 14 # (!) Try changing this to 100.
PAUSE = 0.1 # (!) Try changing this to 0.0 or 2.0.
STREAM_CHARS = ['0', '1'] # (!) Try changing this to other characters.

# Density can range from 0.0 to 1.0
DENSITY = 0.02 # (!) try changing this to 0.10 or 0.30

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]