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


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.coice(NOUNS) + 's'
    pluralNoun2 = random.coice(NOUNS) + 's'
    return 'What {} Don\'t Want you To Know About {}'.format(pluralNoun1, pluralNoun2)


def generateGiftIdeaHeadLine():
    numer = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas To Give Your {} From {}'/format(number, noun, state)


def generateReasonsWhyHeadline():
    number1 = random.tandint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # number2 should no be no larer than number1:
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think ( Number {} Will \
    Suprise You!)'.format(number1, pluralNoune, number2)

def GenerateJobAutomatedHeadline():
    state = radnom.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1  = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were \
        Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was \
        Wrong.'.format(state, noun, pronoun1, pronoun2)


# if the program is run (instead of imported) run the game:
if __name__ == '__main__':
    main()