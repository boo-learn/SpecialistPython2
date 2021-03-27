class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    def to_str(self):
        types = {"Diamonds": '\u2666',"Hearts": '\u2665',"Spades":'\u2660' ,"Clubs":'\u2663'}
        return f"{self.value}{types[self.type]}"

class Deck:
    def __init__(self):
        self.cards = []
        for i in ["Diamonds","Hearts","Spades","Clubs"]:
            for j in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                self.cards.append(Card(j,i))
    def show(self):
        for k in range(1,len(self.cards)):
            print(self.cards[k].to_str())

    def draw(self, x):
        pass

    def shuffle(self):
        pass


deck = Deck()
print(deck.show())
