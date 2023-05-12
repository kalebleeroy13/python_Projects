"""Blackjack, by Al Sweigartwith python.com
The classic card game also know as 21.(This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, card game"""

import random, sys

# Set up the constants:
Hearts = chr(9829) #Character 9829 is '♥'
Diamonds = chr(9830) #Character 9830 is '♦'
Spades = chr(9824) #Character 9824 is '♠'
Clubs = chr(9827) #Character is '♣'
# (A list o fchr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'


def main():
    print('''Blackjack, by Al sweigart al@inventwithpython.com
    
    Rules:
        Try to get as close 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet 
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        Ther dealer stops hitting at 17. ''')

    money = 5000
    while True: # Main game loop.
        # Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        # let the player enter their bet for this round:
        print('Money:', money)
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print('Bet:' , bet)
        while True: # Keep looping intil player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust:
            if getHandValue(playerHand) > 21:
                break
            
            # get the player's move, either H, S, or D:
            move = getMove(playerHand, money - bet) 

            # Handle the player actions:
            if move == 'D':
                # Player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                #Hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank,suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The plasyer has busted:
                    continue

            if move in ('S', 'D'):
                #stand/doubling down stops the player's turn.
                break

        #Handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break # The dealer has busted.
                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        #Handle whether the player won, lost, or tied:
        if dealerValue > 21:
            print('Dealser busts! You win ${}!' .format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You Lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!' .format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')
        
        input('Press Enter to continue...')
        print('\n\n')

def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True: #Keep asking until they enter a valid amount.
        print('How much do you bet? (1-{}, or Quit)' .format(maxBet))
        bet = input('>').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue # if the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Player entered a valid bet. 
        


def getDeck():
    """Return a list of (rank,suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) #ADD the numbered cards. 
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) #Ad the face and ace cards.
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first
    card if showDealerHand is False."""
    print()
    if showDealerHand:
        print('Dealer:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer: ???')
        #Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayHands(playerHand)


def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0] #card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank) #Numbered cards are worth their number.

    # Add the value for the aces:
    value += numberOfAces #Add 1 per ace.
    for i in range(numberOfAces):
        # If another 10 can be added with busting, do so:
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', ''] # The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += '___'  # print the top line of the card.
        if card == BACKSIDE:
            #print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card # The card is a tuple data structure.