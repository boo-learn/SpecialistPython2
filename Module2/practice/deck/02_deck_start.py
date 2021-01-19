import random

class Card:
    types = {
        "diamonds": '\u2666',
        "hearts": '\u2665',
        "spades": '\u2660',
        "clubs": '\u2663',
    }

    values = {"2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "10": 10,
              "J": 10,
              "Q": 10,
              "K": 10,
              "A": 11,
              }

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f"{self.value}{Card.types[self.type]}"


class Deck:
    def __init__(self):
        self.cards = []
        for type in Card.types:
            for value in Card.values:
                self.cards.append(Card(value, type))

    def show(self):
        str = f"desk[{len(self.cards)}]: "
        for card in self.cards:
            str += card.to_str() + ', '
        return str[:-2]

    def draw(self, x):
        pass

    def shuffle(self):
        return random.shuffle(self.cards)


deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())
