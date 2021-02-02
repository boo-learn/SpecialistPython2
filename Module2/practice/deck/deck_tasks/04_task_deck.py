# Сюда отправляем решение четвертой задачи с колодой
#В main.py
print("*"*100)
desk4=Deck(36)
desk5=Deck(36)
# print(desk1.show())
desk4.shuffle()
desk5.shuffle()
print(desk4)
print(desk5)
temp3=[desk4[:1],desk5[:1]]
game_dist={
    'desk4': 0,
    'desk5': 0
}
for temp3,temp4 in zip(desk4,desk5):
    if temp3 > temp4:
        game_dist['desk4'] +=1
    elif temp3 < temp4:
        game_dist['desk5'] += 1
print(game_dist)

# в Desk.py
class Deck:
    def __init__(self,count_card=52):
        self.cards = []
        self.__next_index_card__=0
        for type in [Card.CLUBS, Card.SPADES, Card.HEARTS, Card.DIAMONDS]:
            if count_card == 52:
                for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]:
                    self.cards.append(Card(value , type))
            elif count_card == 36:
                for value in ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]:
                    self.cards.append(Card(value , type))
