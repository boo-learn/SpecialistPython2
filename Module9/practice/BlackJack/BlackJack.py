import random

SPADES_TYPE = "spades"
HEARTS_TYPE = "hearts"
CLUBS_TYPE = "clubs"
DIAMONDS_TYPE = "diamonds"


class Card:
    types = {
        "diamonds": '\u2666',
        "hearts": '\u2665',
        "spades": '\u2660',
        "clubs": '\u2663',
    }
    rank = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
    suit = ("spades", "clubs", "diamonds", "hearts")

    def __init__(self, value, type):
        self.value = value
        self.type = type

        if value == "J" or value == "Q" or value == "K":
            self.score = 10
        elif value == "A":
            self.score = 11
        else:
            self.score = value


    def to_str(self):
        return f"{self.value}{Card.types[self.type]}"

    def __repr__(self):
        return f"{self.value}{Card.types[self.type]}"

    def equal_suit(self, card):
        return self.type == card.type

    def more(self, card2):
        if Card.rank.index(self.value) == Card.rank.index(card2.value):
            return Card.suit.index(self.type) > Card.suit.index(card2.type)
        else:
            return Card.rank.index(self.value) > Card.rank.index(card2.value)

    def __gt__(self, card2):  # >
        if Card.rank.index(self.value) == Card.rank.index(card2.value):
            return Card.suit.index(self.type) > Card.suit.index(card2.type)
        else:
            return Card.rank.index(self.value) > Card.rank.index(card2.value)

    def less(self, card2):
        pass

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type


class Deck:
    def __init__(self):
        self.cards = []

        for type in [HEARTS_TYPE, DIAMONDS_TYPE, CLUBS_TYPE, SPADES_TYPE]:
            for val in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                card = Card(val, type)
                self.cards.append(card)

    def __repr__(self):
        str = f"desk[{len(self.cards)}: ]"
        need_separator = False

        for card in self.cards:
            if need_separator:
                str += ", "
            str += card.to_str()
            need_separator = True

        return str

    def __getitem__(self, index):
        return self.cards[index]

    def show(self):
        str = f"desk[{len(self.cards)}: ]"
        need_separator = False

        for card in self.cards:
            if need_separator:
                str += ", "
            str += card.to_str()
            need_separator = True

        return str

    def draw(self, x):
        # Начало списка карт - верх колоды
        top_cards = []
        for _ in range(x):
            top_cards.append(self.cards.pop(0))
        return top_cards

    def shuffle(self):
        random.shuffle(self.cards)
