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
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f"{self.value}{Card.types[self.type]}"

    def equal_suit(self,card2):
        if self.type == card2.type:
            return True;
        else:
            return False;

    def more(self,card2):
        rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        suit = ["spades","clubs","diamonds","hearts"]

        if rank.index(self.value) > rank.index(card2.value):
            return True;
        elif(rank.index(card2.value) == rank.index(self.value)) and ( suit.index(self.type) > suit.index(card2.type) ):
            return True;
        else:
            return False;

    def less(self,card2):
        rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        suit = ["spades","clubs","diamonds","hearts"]

        if rank.index(self.value) < rank.index(card2.value):
            return True;
        elif(rank.index(card2.value) == rank.index(self.value)) and ( suit.index(self.type) < suit.index(card2.type) ):
            return True;
        else:
            return False;

class Deck:
    def __init__(self):
        self.cards = []

        for type in [HEARTS_TYPE, DIAMONDS_TYPE, CLUBS_TYPE, SPADES_TYPE]:
            for val in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                card = Card(val, type)
                self.cards.append(card)

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
        takecards = [] 
        for i in range(0,x):
            takecards.append(self.cards[i])
        for card in takecards:
            self.cards.remove(card)
        return takecards

    def shuffle(self):
        random.shuffle(self.cards)




card1 = Card("Q", 'hearts')
card2 = Card("A", 'diamonds')
print(card1.more(card2))

deck = Deck()
print('Колода карт')
print(deck.show())
print('Перемешиваем колоду')
deck.shuffle()
print(deck.show())
print('Вытаскиваем 5 карт')
for card in deck.draw(5):
    print(card.to_str())
print('Колода карт')
print(deck.show())
