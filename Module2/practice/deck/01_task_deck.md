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
            return False
        elif (a.type == Card.HEARTS) or (b.type == Card.SPADES):
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
