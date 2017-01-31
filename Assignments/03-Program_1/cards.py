# -*- coding: utf-8 -*-
import random
import pprint

"""
This website gave me the asii idea. 
http://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
"""

"""
@Class AsciiCard 
@Description:
    This class reads 53 (52 cards, and 1 back) ascii representations of a deck of cards from the given file.
@method get_ascii(string,int)
"""
class AsciiCard(object):

    suits = ['Spades','Hearts','Diamonds','Clubs']
    card_faces = []
    
    def __init__(self,cards_file):
        f = open(cards_file, 'r')
        count = 0
        card = ""
        
        for line in f:
            count += 1
            if line.strip() == "":
                continue
            card += line

            if count % 6 == 0:
                self.card_faces.append(card)
                card = ""
        # pp = pprint.PrettyPrinter(depth=6)
        # pp.pprint(self.card_faces)

    """
    @Description:
        This method takes a card suit, and an integer between 2,14 inclusive and 
        returns the corresponding ascii representation of that card. 
    @Example:
        print(a.get_ascii('Spades',7)) 
            _____
            |7    |
            | ♠ ♠ |
            |♠ ♠ ♠|
            | ♠ ♠ |
            |____L|
            
        print(a.get_ascii('Clubs',14))
            _____
            |A _  |
            | ( ) |
            |(_♣_)|
            |  |  |
            |____V|
    """
    def get_ascii(self,suit=None,rank=None):
        if suit == None or rank == None:
            return self.card_faces[0] ;
        s_index = self.suits.index(suit)
        return self.card_faces[((s_index * 13) + rank) - 1] ;
        
    
        
"""
@Class Card 
@Description:
    
"""
class Card(AsciiCard):
    ranks = [None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]
    name_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

    def __init__(self, suit='', rank=0):
        super().__init__('ascii_cards.txt')
        
        # If user passes in an int between 0-3, then convert it to string
        # otherwise keep the string 
        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit
            
        self.rank = rank
        self.symbol = self.name_to_symbol[self.suit]
        self.card = self.get_ascii(self.suit,self.rank)

    def __str__(self):
        return (self.card)
           
    def __cmp__(self,other):
        t1 = self.suit,self.rank
        t2 = other.suit,other.rank
        return int(t1[1])<int(t2[1])
   
    # Python3 wasn't liking the __cmp__ to sort the cards, so 
    # documentation told me to use the __lt__ (less than) 
    # method.
    def __lt__(self,other):
        return self.__cmp__(other)

        
"""
@Class Deck 
@Description:
    This class represents a deck of cards. 
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""       
class Deck(object):
    def __init__(self):
        #assume top of deck = 0th element
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
        return self.cards.pop(0)
        
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards = sorted(self.cards)

if __name__=='__main__':
    c = Card('Clubs',14)
    print(c)

    