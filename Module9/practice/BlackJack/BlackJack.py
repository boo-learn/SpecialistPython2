from cards.classes.Card import Card
from cards.classes.Deck import Deck
import json


class BJ_Card(Card):
    def getvalue(self: Card, hand_score):
        if self.value in {"K", "Q", "J"}:
            return 10
        if self.value == "A":
            return 1 if hand_score > 10 else 11
        return int(self.value)


class BJ_Deck(Deck):
    card_class = BJ_Card

    def calculate_score(self):
        player_score = 0
        for card in self:
            player_score += card.getvalue(player_score)
        player_score_aces = 0
        for card in self:
            player_score_aces += card.getvalue(player_score)
        return player_score_aces


# deck = Black_Jack_Deck(Deck)


# json.loads()


player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки
# a = Card("2",Card.HEARTS)
playing_deck = BJ_Deck()
while True:
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    playing_deck.shuffle()
    # 2. Игроку выдаем две карты
    player_cards = playing_deck.draw(2)

    player_score = player_cards.calculate_score
    # 3. Дилер берет одну карту
    dealer_cards = playing_deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(f"player: {player_cards}")
    print(f"dealer: {dealer_cards}")
    print(f"remain_cards: {playing_deck}")
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    blackjack = player_cards.calculate_score == 21
    if blackjack:
        # Выплачиваем выигрыш 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = None
        while not player_choice:
            try:
                _ = input("1:еще/2:достаточно: ")
                player_choice = int(_)
                if player_choice > 2:
                    raise ValueError("Expect 1 or 2")
            except ValueError as e:
                print(f"Incorrect input: {e}")
        # if player_choice.lower() == "еще" or player_choice.lower() == "ещё":
        if int(player_choice) == 1:

            # Раздаем еще одну карту
            player_cards += playing_deck.draw(1)
            print(f"Player:{player_cards}")
            # Если перебор (>21), заканчиваем добор
            if player_cards.calculate_score() == 21:
                break
        if int(player_choice) == 2:
            print(playing_deck)
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    dealer_wins = False
    if player_cards.calculate_score() > 21:
        dealer_wins = True
    while True:  # дилер начинает набирать карты.
        if dealer_wins:
            break
        dealer_cards += playing_deck.draw(1)
        print("Deale Cards", dealer_cards)
        if dealer_cards.calculate_score() >= 17:
            break
        if dealer_cards == 21:
            dealer_wins = True
        ...  # Смотри подробные правила добора дилера в задании

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
