# Сюда отправляем решение второй задачи с колодой
from Classes.Deck import Deck

HEARTS = '\u2665'
DIAMONDS = '\u2666'
CLUBS = '\u2663'
SPADES = '\u2660'
types = [SPADES, CLUBS, DIAMONDS, HEARTS]

deck=Deck()
print(f'Исходная колода {deck}')
deck.shuffle()
print(f'После перемешивания {deck}')
ten_cards=deck[:10]
print(f'Десять карт: {ten_cards}')

counter=[]
for type in types:
    count=0
    for card in ten_cards:
        if card.type==type:
            count+=1
    counter.append(count)

print(f'Максимальное количество карт одной масти {max(counter)}')
print('в мастях: ',sep='')
i=0
for count in counter:
    if count==max(counter):
        print(types[i],sep='')
    i+=1
