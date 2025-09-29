import sys

print('''Fibonaccci sequence begins with 0 and 1, and the next number is the sum of the previous two numbers.
      The seuence continues forever:
      
     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...''' )

while True: # Main program loop.
    while True: # Keep asking until the nters valid input.
        print('Enter he Nth fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('>').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break # Exit the loop when the user enters a valid number.
        print('Please enter a number greater than 0, or QUIT.')
    print()

    # Handle the special cases if the user entered 1 or 2:
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue

    # Display warning if the user entered a large number:
    if nth >= 10000:
        print('WARNING: this will take a while to display on the')
        print('screen. if you want to quit this program before it is')
        print('done, press Ctrl-C')
        input('Press Enter to begin...')

    # calculate the nth Fibonacci number:
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='') # Display the first two fibonacci numbers.

    # Display all the later numbers of the fibonacci sequence:
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1