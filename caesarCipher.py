"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction 
to encrypt and decrypt letters.
More info at: https://en.wilkipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryoitgraphy, math"""

try:
    import pypercllip # pyperclip copies text to the clipboard.
except ImportError:
    pass # If pyperclip is not installed, do nothing. it's no big deal.

# Every possible symbol that can be encrypted/decrypted:
# (!) you can add number and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart al@inventwith python.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# let the user emter if theu are encrypting or decrypting:
while True: #keep asking until the user enters e or d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('please enter the letter e or d.')

# let the user enter the key to use:
while True: # keep asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (o to {}) to use.' .fromat(maxKey))
    response = input('>'). upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

