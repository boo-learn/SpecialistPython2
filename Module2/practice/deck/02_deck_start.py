SPADES_TYPE = "spades"
HEARTS_TYPE = "hearts"
CLUBS_TYPE = "clubs"
DIAMONDS_TYPE = "diamonds"


class Card:

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        TYPES_DICT = {SPADES_TYPE: "♠", HEARTS_TYPE: "♥", CLUBS_TYPE: "♣",
                      DIAMONDS_TYPE: "♦"}

        return f"{self.value}{TYPES_DICT[self.type]}"


class Deck:
    def __init__(self):
        self.cards = []

        for type in [HEARTS_TYPE,DIAMONDS_TYPE,CLUBS_TYPE,SPADES_TYPE]:
            for val in [range(2,8)]:
                self.cards.append(Card(val, type))

            for val in ["J", "Q", "K", "A"]:
                self.cards.append(Card(val, type))

    def show(self):
        str = f"desk[{len(self.cards)}: ]"
        need_separator = False

        for card in self.cards:

            if need_separator:
                str += ", "

            str += f"{card.to_str()}"
            need_separator = True

        return str
            #метод .show() - отображает все карты колоды в формате: deck[12]: 3♥, 4♦, A♣, …

    def draw(self, x):
        pass

    def shuffle(self):
        pass


deck = Deck()
print(deck.show())
deck.shuffle()
print(deck.show())
