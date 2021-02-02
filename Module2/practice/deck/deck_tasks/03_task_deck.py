# Сюда отправляем решение третьей задачи с колодой
from Classes.Deck import Deck

deck=Deck()
print(f'Исходная колода {deck}')
deck.shuffle()
print(f'Первое перемешивание {deck}')
first_card=deck.draw(1)
print(f'Первая карта: {first_card}')
deck.shuffle()
print(f'Второе перемешивание {deck}')
second_card=deck.draw(1)
print(f'Вторая карта: {second_card}')

while first_card>second_card:
    deck.shuffle()
    print(f'Следующее перемешивание {deck}')
    first_card=second_card
    second_card_card = deck.draw(1)
    print(f'Следующая карта: {second_card}')
