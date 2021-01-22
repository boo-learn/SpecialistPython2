card_types = {"hearts": ('Червы','\u2661'),
                 "diamonds": ('Бубны', '\u2662'),
                 "clubs": ('Трефы', '\u2663'),
                 "spades": ('Пики', '\u2660'),
             }
    
# priority     "hearts" > "diamonds" > "clubs" > "spades"
card_types_prio = ("hearts","diamonds","clubs", "spades")

# priority    2 < 3 < ... < 'A'
card_values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')


class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f"{self.value}{card_types[self.type][1]}"
    
    def equal_suit(self, card):
        if self.type == card.type:
            return True
        else:
            return False
        
    def more(self, card):
        index_self_v = card_values.index(self.value)
        index_card_v = card_values.index(card.value)
        index_self_t = card_types_prio.index(self.type)
        index_card_t = card_types_prio.index(card.type)
        if index_self_v > index_card_v:
            return True
        elif index_self_v == index_card_v and index_self_t < index_card_t:
            return True
        else:
            return False
        

class Deck:

    def __init__(self):
        self.cards = []

        for type in card_types:
            for val in card_values: 
                card = Card(val, type)
                self.cards.append(card)

    def show(self):
        str = f"desk[{len(self.cards)}]: "
        need_separator = False

        for card in self.cards:
            if need_separator:
                str += ", "
            str += card.to_str()
            need_separator = True

        return str

    def draw(self, x):
        list_draw = []
        
        if x <= len(self.cards):
            for _ in range(x):
                list_draw.append(self.cards[0].to_str())
                del self.cards[0]
        else:
            print(f'Error: length of Deck {len(self.cards)} less than {x}')
        return list_draw
        

    def shuffle(self):
        pass


card1 = Card(9, 'spades') # hearts
card2 = Card('A', 'spades') # diamonds

print(card1.equal_suit(card2)) 

print(card1.more(card2))

print(card1.to_str())

deck = Deck()
print(deck.show())

print(deck.draw(5))

print(deck.show())


# deck.shuffle()
# print(deck.show())

print(card_types)
