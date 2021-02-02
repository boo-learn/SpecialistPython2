# Сюда отправляем решение третьей задачи с колодой
from classes.Card import Card
from classes.Deck import Deck

deck = Deck()
print(deck)
deck.shuffle()

prev_card = deck.draw(1)[0]
card = None

while True:
    deck.shuffle()
    card = deck.draw(1)[0]
    print(f"Предыдущая карта {prev_card.to_str()}, вытянутая карта {card.to_str()}")
    if card > prev_card:
        break

print(f"{card.to_str()} больше {prev_card.to_str()}")
