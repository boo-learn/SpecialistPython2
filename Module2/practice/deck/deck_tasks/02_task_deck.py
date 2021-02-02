# Сюда отправляем решение второй задачи с колодой
from classes.Card import Card
from classes.Deck import Deck

deck = Deck()
print(deck)
deck.shuffle()
print(deck)
hand = deck.draw(10)

types = [[0, Card.HEARTS],  [0, Card.DIAMONDS], [0, Card.CLUBS], [0, Card.SPADES]]

for card in hand:
    if card.type == Card.HEARTS:
        types[0][0] += 1
    if card.type == Card.DIAMONDS:
        types[1][0] += 1
    if card.type == Card.CLUBS:
        types[2][0] += 1
    if card.type == Card.SPADES:
        types[3][0] += 1

types.sort(reverse=1)

print(hand)

print(f"{types[0][1]} - больше")
