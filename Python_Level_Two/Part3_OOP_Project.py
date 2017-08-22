#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle
import itertools

# Two useful variables for creating Cards.
SUIT = 'Hearts Diamonds Spades Clubs'.split()
RANKS = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print('Creating New Deck...')
        self.allcards = [' of '.join(a) for a in itertools.product(RANKS, SUIT)]

    def shuffle(self):
        print('Shuffling Cards...')
        shuffle(self.allcards)

    def split_in_half(self):
        print('Dealing Cards...')
        return (self.allcards[:26], self.allcards[26:])

class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def remove_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

class Player():
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def has_cards(self):
        return len(self.hand) != 0

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print('->{} has played the {}'.format(self.name, drawn_card)),
        return drawn_card

    def remove_war_cards(self, num_cards=4):
        war_cards = []
        # if len(self.hand) < 4:
        #     for x in range(len(self.hand)):
        #         war_cards.append(self.hand.remove_card())
        #     return war_cards
        # else:
        for x in range(num_cards):
            war_cards.append(self.hand.remove_card())
        return war_cards


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

d = Deck()
d.shuffle()
p1cards, p2cards = d.split_in_half()

computer = Player('Computer', Hand(p1cards))
player = Player(input('Enter your name >> '), Hand(p2cards))
# player = Player('T', Hand(p2cards))

total_rounds = 0
war_rounds = 0

# This is there where the while loop will start

while player.has_cards() and computer.has_cards():

    print('\nHere are the stats so far:')
    print('Total Rounds: {}\nWar Rounds: {}'.format(total_rounds, war_rounds))
    print('{} has {} cards remaining\n{} has {} cards remaining'.format(player.name,
                                                                        len(player.hand),
                                                                        computer.name,
                                                                        len(computer.hand)))

    print('\nStarting new round:')
    total_rounds += 1
    cards_on_table = []

    player_card = player.play_card()
    computer_card = computer.play_card()

    cards_on_table.extend((player_card, computer_card))

    if RANKS.index(player_card.split()[0]) > RANKS.index(computer_card.split()[0]):
        print('{} has the higher card'.format(player.name))
        player.hand.add_card(computer_card)
    elif RANKS.index(player_card.split()[0]) < RANKS.index(computer_card.split()[0]):
        print('{} has the higher card'.format(computer.name))
        computer.hand.add_card(player_card)
    else:
        war_rounds += 1
        print('Cards ranks are the same: WAR TIME!')
        min_cards_left = min(len(player.hand), len(computer.hand))
        if min_cards_left < 4:
            cards_to_draw = min_cards_left
        else:
            cards_to_draw = 4
        cards_on_table.extend(player.remove_war_cards(cards_to_draw))
        player_card = cards_on_table[-1]
        cards_on_table.extend(computer.remove_war_cards(cards_to_draw))
        computer_card = cards_on_table[-1]

if player.has_cards():
    print('\n----------------------\n\n{} is the WINNER!'.format(player.name))
else:
    print('\n----------------------\n\n{} is the WINNER! Better luck next time.'.format(computer.name))

print('Total Rounds: {}\nWar Rounds: {}'.format(total_rounds, war_rounds))
