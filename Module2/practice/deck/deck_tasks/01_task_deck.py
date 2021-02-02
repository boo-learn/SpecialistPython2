# Сюда отправляем решение первой задачи с колодой
from Classes.Deck import Deck

deck=Deck()
print(f'Исходная колода {deck}')
deck.shuffle()
print(f'После перемешивания {deck}')
two_cards=deck[:2]
print(f'Две карты: {two_cards}')
if two_cards[0]>two_cards[1]:
    print(f' карта {two_cards[0]} больше {two_cards[1]}')
else:
    print(f' карта {two_cards[1]} больше {two_cards[0]}')
