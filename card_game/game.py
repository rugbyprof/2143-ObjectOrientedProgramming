import random

class Card(object):
    suits = ('Heart','Diamond','Spade','Club')
    ranks = [None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
        
    def __cmp__(self,other):
        t1 = self.suit,self.rank
        t2 = other.suit,other.rank
        
        #return cmp(t1,t2)
        return cmp(t1[1],t2[1])
        
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
    print(card1>card2)
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
        print(hands[i])
        
    print len(deck.cards)