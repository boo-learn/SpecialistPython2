class Card:
    dic_types = {"Hearts": ('Червы','\u2661', '\u2665'),
                 "Diamonds": ('Бубны', '\u2662', '\u2666'),
                 "Clubs": ('Трефы','\u2667', '\u2663'),
                 "Spades": ('Пики','\u2664', '\u2660'),
         }
    
    dic_value = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f'{self.value} {Card.dic_types[self.type][1]}'


class Deck:
    def __init__(self):
        self.cards = []
        for v in Card.dic_value:
            for t in Card.dic_types:
                self.cards.append(Card(v,t))

    def show(self):
        
        return self.cards

    def draw(self, x):
        pass

    def shuffle(self):
        pass

s = Card(2,"Diamonds")
print(s.to_str())

deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())
