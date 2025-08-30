"""An art program that draws a continuos line around the screen using the
WASD keys. Inspired by Etch A Sketch toys.

For example, you can draw Hilbert Curve fractal with:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

 larger Hilbert Curve fractal with:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD"""

import shutil, sys

# Set ip the constants for the line chatacters:
UP_DOWN_CHAR            = chr(9474) # Character 9474 is '|'
LEFT_RIGHT_CHAR         = chr(9472) # Character 9472 is '-'
DOWN_RIGHT_CHAR         = chr(9484) # Character 9484 is '┌'
DOWN_LEFT_CHAR          = chr(9488) # Character 9488 is '┐'
UP_RIGHT_CHAR           = chr(9492) # Character 9492 is '└'
UP_LEFT_CHAR            = chr(9496) # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR      = chr(9500) # Character 9500 is '├'
UP_DOWN_LEFT_CHAR       = chr(9508) # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR    = chr(9516) # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR      = chr(9524) # Character 9524 is '┴'
CROSS_CHAR              = chr(9532) # Character 9532 is '┼'

