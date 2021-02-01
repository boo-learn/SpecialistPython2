import pprint
import random

class Card:
    HEARTS = '\u2665'
    DIAMONDS = '\u2666'
    CLUBS = '\u2663'
    SPADES = '\u2660'

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
         return f"{self.value}{self.type}"


class Deck:
    def __init__(self):
        self.cards = []
        for type in [Card.CLUBS, Card.SPADES, Card.HEARTS, Card.DIAMONDS]:
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т' ]:
                self.cards.append(Card(value, type))

    def show(self):
        print(len(self.cards), 'in deck')
        for card in self.cards:
            print(card.to_str())

    def draw(self, x):
        i = 0
        while i != x:
            print(self.cards[i].to_str())
            i += 1

    def shuffle(self):
        shuffled_deck = []
        for card in self.cards:
            shuffled_deck.insert(random.randint(1, 54+1), card)
        self.cards = shuffled_deck


#card1 = Card(3, Card.CLUBS)
#print(card1)
#print(card1.to_str())
deck = Deck()
deck.show()
print('=============')
deck.draw(5)
print('=============')
deck.shuffle()
deck.show()
