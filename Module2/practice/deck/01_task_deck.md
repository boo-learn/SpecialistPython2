import random


class Card:
    SPADES = "\u2660"
    HEARTS = "\u2665"
    CLUBS = "\u2663"
    DIAMONDS = "\u2666"
    J = 11
    Q = 12
    K = 13
    A = 14

    @staticmethod
    def suit_greater_then(a, b):
        """
            # 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
            # ♥ > ♦ > ♣ > ♠"""
        # исключим равенство мастей
        if not a.equal_suit(b):

            if (a.type == Card.HEARTS) or (b.type == Card.SPADES):
                return True
            elif (a.type == Card.SPADES) or (b.type == Card.HEARTS):
                return False
            elif a.type == Card.DIAMONDS:
                if b.type == Card.CLUBS:
                    return True
                else:
                    return False

    def equal_suit(self, other):
        return self.type == other.type

    def __init__(self, value, type):
        value = str(value)
        self.type = type
        if value.lower() == "j":
            self.value = Card.J
            return
        if value.lower() == "q":
            self.value = Card.Q
            return
        if value.lower() == "k":
            self.value = Card.K
            return
        if value.lower() == "a":
            self.value = Card.A
            return
        self.value = int(value)

    def __repr__(self):
        return self.to_str()

    def to_str(self):
        return f"{self.value}{self.type}"

    def less(self, other_card):
        if self.value < other_card.value:
            return True
        elif self.value == other_card.value:
            return not Card.suit_greater_then(self, other_card)
        else:
            return False

    def more(self, other_card):

        if self.value > other_card.value:
            return True
        elif self.value == other_card.value:
            return Card.suit_greater_then(self, other_card)
        else:
            return False


class Deck:
    def __init__(self):
        self.cards = []
        for type in [Card.CLUBS, Card.SPADES, Card.HEARTS, Card.DIAMONDS]:
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(value, type))

    def show(self):
        deck_str = f"deck[{len(self.cards)}]:"
        for card in self.cards:
            deck_str += card.to_str()
        return deck_str

    def draw(self, x):
        hand = []
        for _ in range(x):
            card = self.cards.pop(0)
            hand.append(card)
        return hand

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())

c = Card('2', Card.DIAMONDS)
print(c)
d = Card(2,Card.SPADES)
print(d)

print(c.more(d))
