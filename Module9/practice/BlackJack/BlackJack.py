from card_deck import Deck, Card
import json

#json.loads()

# # метод для класса Card
# def get_blackjack_value(self, points):
#     if self.value in ('2', '3', '4', '5', '6', '7', '8', '9', '10'):
#         return int(self.value)
#     elif self.value == "A":
#         if points <= 21:
#             return 11
#         else:
#             return 1
#     else:
#         return 10

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

deck = Deck()
blackjack = False

def count_bj_points(card_pool, points=0):
    for card in card_pool:
        points += card.get_blackjack_value(points)
    return points

while True:
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    deck.shuffle()
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(f"player's cards are: {player_cards}\ndealer's cards are: {dealer_cards}")

    points = count_bj_points(player_cards)
    #for card in player_cards:
        #points += card.get_blackjack_value(points)
    print("total after 1st:", points)
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if points == 21:
        blackjack = True
    if blackjack:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        break
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще/достаточно: ")
        if player_choice.lower() == "еще" or player_choice.lower() == "ещё":
            # Раздаем еще одну карту
            player_cards = deck.draw(1)
            points = count_bj_points(player_cards, points)
            print("total after 2nd",points, player_cards)
            # Если перебор (>21), заканчиваем добор
            if points > 21:
                print(f"Too much - {points}")
                break
        if player_choice.lower() == "достаточно":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    while True:  # дилер начинает набирать карты.
        break  # Смотри подробные правила добора дилера в задании

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
