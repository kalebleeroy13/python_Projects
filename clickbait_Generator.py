"""Clickbait Headline Generator, by Ai Sweigart al@inventwithpython.com
a clickbait headline generator for your souless content farm website.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, beginner, humor, word"""

import random

# Setup the constants:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
            'Illinois', 'Ohio', 'Georgia', 'North Carollina', 'Michigan']
NOUNS = ['Athletes', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
            'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
            'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement', 
            'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'Right Now', 'Next Week']


def main():
    print('Clickbait Headline Generator')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break # Exit the loop once a valid number is entered.

    for i in range(numberOfHeadlines):
        clickbaitType = random.randit(1, 8)

        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickBaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickBaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickBaitType == 4:        
            headline = generateYouWontBelieveHeadLine()
        elif clickBaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickBaitType == 6:
            headline = generateGiftIdealine()
        elif clickBaitType == 7:
            headline = generateReasonWhyHeadline()
        elif clickBaitType == 8:                
            headline = generateJobAutomaedHeadline()

        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebukk', 'Googles',
                            'Facesbook','Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')


# Each of these functions returns a different type of headline:
def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millennials Killin the {} Industry?'.format(noun)

def generateWhatYouDontKnowHeadline():
    noun = Random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could kill you {}'.format(noun, pluralNoun, when)



def generateBigCompaniesHateHerHeadline():
    pronoun = randomchoice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How this {} {} Invented a Cheaper {}'.format
    (pronoun, state , noun1, noun2)

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSEIVE_PRONOUNS)
    return 'You Won\'t Believe What This {} {}Found in {} {}'.format
    (state, noun, pronoun, place)