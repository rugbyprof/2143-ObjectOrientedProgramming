# -*- coding: utf-8 -*-
import random

CARD_TEMPLATE = """\
┌─────────┐
│{}       │
│         │
│         │
│    {}   │
│         │
│         │
│       {}│
└─────────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

HIDDEN_CARD_TEMPLATE = """\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"""

def join_lines(strings):
    """
    Stack strings horizontally.
    This doesn't keep lines aligned unless the preceding lines have the same length.
    :param strings: Strings to stack
    :return: String consisting of the horizontally stacked input
    """
    liness = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*liness))

def ascii_version_of_card(*cards):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :return: A string, the nice ascii version of cards
    """

    # we will use this to prints the appropriate icons for each card
    name_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

    def card_to_string(card):
        # 10 is the only card with a 2-char rank abbreviation
        rank = card.rank if card.rank == '10' else card.rank[0]

        # add the individual card on a line by line basis
        return CARD.format(rank=rank, suit=name_to_symbol[card.suit])


    return join_lines(map(card_to_string, cards))


def ascii_version_of_hidden_card(*cards):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """

    return join_lines((HIDDEN_CARD, ascii_version_of_card(*cards[1:])))

class Card(object):
    suits = ('Hearts','Diamonds','Spades','Clubs')
    ranks = [None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]
    name_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
        self.symbol = self.name_to_symbol[self.suits[self.suit]]
        self.card = CARD_TEMPLATE.format(rank=self.rank, suit=self.symbol+' ')

    def __str__(self):
        return (self.card)
   
    def pprint(self):
        lines = self.card
        return lines.splitlines()
        
    def __cmp__(self,other):
        t1 = self.suit,self.rank
        t2 = other.suit,other.rank
        
        return self.compare(t1,t2)
        
    def compare(self,t1,t2):      
        return t1[1] < t2[1]     
        
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return " ".join(res)
    
    def pop_card(self):
        return self.cards.pop()
        
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards = sorted(self.cards)

class Hand(Deck):
    def __init__(self,label=''):
        self.cards = []
        self.label = label
        
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        res = " ".join(res)
        return self.label + "::" + res
    
        
if __name__=='__main__':
    card1 = Card(2,12)
    card2 = Card(3,13)
    print(card2)
    deck = Deck()
    #print(deck)
    deck.shuffle()
    #print(deck)
    hands = []
    for i in range(5):
        hands.append(Hand(str(i)))
        for j in range(5):
            hands[i].add_card(deck.pop_card())
        
    for i in range(5):
        hands[i].sort()
        #print(hands[i])
        
    print(len(deck.cards))
    #print(HIDDEN_CARD)
    
    string1 = card1.pprint()
    string2 = card2.pprint()
    string3 = []
    for i in range(len(string1)):
        string3.append(string1[i]+string2[i])
        
    for line in string3:
        print(str(line))