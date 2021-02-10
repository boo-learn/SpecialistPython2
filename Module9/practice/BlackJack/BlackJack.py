from Deck import Deck, Card
# import json
# json.loads()

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

player_summ = 0
dealer_summ = 0

dealer_blackjack = False

deck = Deck()

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
    blackjack = deck.is_blackjack(player_cards)
    print(f"Карты игрока {player_cards}")
    print(f"Карты дилера {dealer_cards}")
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if blackjack:
        # Выплачиваем выигрыш 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        # Заканчиваем игру
        print(f"Баланс игрока {player_money}")
        player_blackjack = True
        break

    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice.lower() == "1":
            # Раздаем еще одну карту
            # Если перебор (>21), заканчиваем добор
            player_cards += deck.draw(1)
            player_summ = deck.summ(player_cards)
            print(f"Карты игрока {player_cards} сумма {player_summ}")
            print(f"Карты дилера {dealer_cards}")
            if player_summ > 21:
                print(f"перебор. Игрок проиграл. Конец игры.")
                break
        if player_choice.lower() == "0":
            # Заканчиваем добирать карты
            break

    if blackjack or player_summ > 21:
        break

    print(f"Карты игрока {player_cards} сумма {player_summ}")

    # Если у игрока не 21(блэкджек) и нет перебора, то
    while True:  # дилер начинает набирать карты.
        # Смотри подробные правила добора дилера в задании
        dealer_cards += deck.draw(1)
        if deck.is_blackjack(dealer_cards):
            print("Black Jack. Казино победило")
            # Заканчиваем игру
            break
        dealer_summ = deck.summ(dealer_cards)
        print(f"Карты дилера {dealer_cards} сумма {dealer_summ}")
        if (dealer_summ >= 17):
            break

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if player_summ > dealer_summ:
        print("Игрок победил")
        player_money += rate_value
        break
    if player_summ < dealer_summ:
        print("Казино победило")
        player_money += rate_value
        break
    print("Ничья")

    
    

    def is_blackjack(self, cards):
        flag_a = False
        flag_10 = False
        for card in cards:
            if card.value == 'A':
                flag_a = True
            if card.value in ('10', 'J', 'Q', 'K'):
                flag_10 = True
        if flag_a and flag_10:
            return  True
        return False

    def summ(self, cards):
        summ = 0
        for card in cards:
            if card.value in ('2', '3', '4', '5', '6', '7', '8', '9', '10'):
                summ += int(card.value)
            if card.value in ('J', 'Q', 'K'):
                summ += 10
            if card.value == 'A':
                if summ > 21:
                    summ += 1
                else:
                    summ += 11
        return summ
