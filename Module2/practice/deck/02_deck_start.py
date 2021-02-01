class Card:
    HEARTS='Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'
    def __init__(self, value, type):
        self.value = value
        self.type=type

    def to_str(self):
        if self.type == Card.HEARTS: self.type = '\u2665'
        if self.type == Card.DIAMONDS: self.type = '\u2666'
        if self.type == Card.CLUBS: self.type = '\u2663'
        if self.type == Card.SPADES: self.type = '\u2660'
        return f'{self.value}{self.type}'


class Deck:
    def __init__(self):
        self.cards = []

    def show(self):
        pass

    def draw(self, x):
        pass

    def shuffle(self):
        pass


deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())
