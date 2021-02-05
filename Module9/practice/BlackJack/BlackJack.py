import random
from classes.Card import Card

class BJCard(Card):
    def __init__(self,value, type,point):
        super(BJCard, self).__init__(value, type)
        self.point=point
    def __repr__(self):
        return f'{self.value}{self.type}'

class Deck:
    def __init__(self,count_card=52):
        self.cards = []
        self.__next_index_card__=0
        for type in [Card.CLUBS, Card.SPADES, Card.HEARTS, Card.DIAMONDS]:
            if count_card == 52:
                for value in ['2', '3', '4', '5','6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                    self.cards.append(Card(value , type))
            elif count_card == 36:
                for value in ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]:
                    self.cards.append(Card(value , type))

    def __repr__(self):
        deck_str = f"deck[{len(self.cards)}]:"
        for card in self.cards:
            deck_str += card.__repr__()
        return deck_str

    def draw(self, x):
        hand = []
        for _ in range(x):
            try:
                card = self.cards.pop(0)
                hand.append(card)
            except IndexError or TypeError:
                print("Колода закончилась")
                return []
        return hand

    def __getitem__(self, item):
        if isinstance(item,slice):
            # print(slice.start)
            # print(slice.stop)
            # print(slice.step)
            return self.cards[item]
        return self.cards[item]
        # x=slice(start=x,stop=y,step=z)
        # for _ in range(x):
        #     card = self.cards.pop(0)
        #     hand.append(card)
        # return hand

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        self.__next_index_card__ = 0
        return self

    def __next__(self):
        try:
            card = self.cards[self.__next_index_card__]
        except IndexError:
            raise StopIteration
        self.__next_index_card__+=1
        return card

class BJDeck(Deck):
    def __init__(self,count_card=52):
        self.cards = []
        self.__next_index_card__ = 0
        for type in [Card.CLUBS, Card.SPADES, Card.HEARTS, Card.DIAMONDS]:
            if count_card == 52:
                for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                    self.cards.append(BJCard(value, type, point=int(value)))
                for value in ['A']:
                    self.cards.append(BJCard(value, type, point=int(11)))
                for value in ['J', 'Q', 'K']:
                    self.cards.append(BJCard(value, type, point=int(10)))
