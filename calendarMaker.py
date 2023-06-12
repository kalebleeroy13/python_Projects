"""Calendar Maker, by Al sweigart al@inventwithpython.com
Create monthly calendars, saved to textfile and fit for printing. 
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short"""

import datetime

# set up the constants:
DAYS = ('Sunday ','Monday','Tuesday', 'Wendnesday', 'Thursday ',
        'Friday ', 'Saturday ')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Alsweigart al@inventwithpython.com')

while True: # loop to get a year from the user. 
    print('Enter the year for the calendar:')
    response = input('> ')

    if reponse.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023.')
    continue

while True: # Loop to get  a year from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def getCalendarfor(year,month):
    calText = '' #calText eill contain the string of our calendar.

    # Put the month and year at the top of the calendar:
    calText += (' ' * 34) + Months[month - 1] + ' ' + str(year) + '\n'
    
    # Add the days of the week labels to the calendar:
    # (!) Try changing this to abbreviations : SUN, MON, TUE, etc.
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal line string that seperate weeks:
    weekSeperator = ('+----------' * 7) + '\n'

    # The blank rows have ten spaces in between the | day sperators:
    blankRow = ('|          ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all 
    # the complicated calendar stuff for us here.)
    currentDat = datetime.date(year,month, 1)

    # Roll back currentDate until it is Sunday. (weekday() returns 6
    # for Sunday not 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(day=1)

    while true: # Loop over each week in the month.
        calText += weekSeperator

        # dayNumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) #go to next day.
            dayNumberRow += '|\n' #Add the vertical line after Saturday.

            # Add the day number row and 3 blank rows to the calendar tex.
            calText += blankRow
            for i in range(3): # (!) Try changing the 3 to a 5 or 10.
                calText += blankRow

            # Check if we're done with the month:
            if currentDate.month != month:
                break

    # Add the horizontal line at the very bottom of the calendar
    calText =+ weekSeperator
    return calText



    