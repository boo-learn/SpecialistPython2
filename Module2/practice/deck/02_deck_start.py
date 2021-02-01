class Card:
    SPADES = "\u2660"
    HEARTS = "\u2665"
    CLUBS = "\u2663"
    DIAMONDS = "\u2666"
    J = 11
    Q = 12
    K = 13
    A = 14
    def __init__(self, value, type):
        self.type = type
        if value is int:
            self.value = value
        if value.lower() == "j":
            self.value = Card.J
        if value.lower() == "q":
            self.value = Card.Q
        if value.lower() == "k":
            self.value = Card.K
        if value.lower() == "a":
            self.value = Card.A



    def to_str(self):
        return f"{self.value}{self.type}"

    def compare(self):

        # 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
        # ♥ > ♦ > ♣ > ♠


