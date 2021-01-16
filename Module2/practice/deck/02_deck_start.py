import random


values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
types = {'hearts': '\u2665',
         'diamonds': '\u2666',
         'clubs': '\u2663',
         'spades': '\u2660'}


class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f"{self.value} {types[self.type]}"


class Deck:
    def __init__(self):
        self.cards = []

        for type in types:
            for value in values:
                card = Card(value, type)
                self.cards.append(card)

    def show(self):
        print(f'deck[{len(self.cards)}]: {[card.to_str() for card in self.cards]}')

    def draw(self, x):
        drawed = []
        for i in range(x):
            out = self.cards.pop(i)
            drawed.append(out.to_str())
        return drawed

    def shuffle(self):
        return random.shuffle(self.cards)


def main():
    deck = Deck()

    print(deck.show())
    deck.shuffle()
    print(f'DRAW: {deck.draw(5)}')
    print(deck.show())



if __name__ == '__main__':
    main()
