# from cards.classes.Card import Card
# from cards.classes.Deck import Deck
import json
import random

class Card:
    HEARTS = '\u2665'
    DIAMONDS = '\u2666'
    CLUBS = '\u2663'
    SPADES = '\u2660'
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    types = [SPADES, CLUBS, DIAMONDS, HEARTS]

    def __init__(self, value, type):
        self.value = str(value)
        self.type = type

    def to_str(self):
        return f'{self.value}{self.type}'

    def __repr__(self):
        return f'{self.value}{self.type}'

    def equal_suit(self, card):
        return self.type == card.type

    def more(self, card):
        # if Card.values.index(self.value) > Card.values.index(card.value):
        #     return True
        # elif Card.values.index(self.value) < Card.values.index(card.value):
        #     return False
        # else:
        #     return Card.types.index(self.type) > Card.types.index(card.type)

        if Card.values.index(self.value) == Card.values.index(card.value):
            return Card.types.index(self.type) > Card.types.index(card.type)
        return Card.values.index(self.value) > Card.values.index(card.value)

    def __gt__(self, card):
        if Card.values.index(self.value) == Card.values.index(card.value):
            return Card.types.index(self.type) > Card.types.index(card.type)
        return Card.values.index(self.value) > Card.values.index(card.value)

    def __lt__(self, card):
        if Card.values.index(self.value) == Card.values.index(card.value):
            return Card.types.index(self.type) < Card.types.index(card.type)
        return Card.values.index(self.value) < Card.values.index(card.value)

    def less(self, card):
        pass


class Deck:
    card_class = Card
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, lst=[]):
        self.cards = lst
        if self.cards:
            return
        self.__nextindex = 0
        for type in [self.card_class.CLUBS, self.card_class.SPADES, self.card_class.HEARTS, self.card_class.DIAMONDS]:
            for value in self.values:
                self.cards.append(self.card_class(value, type))

    def __repr__(self):
        return Deck.show(self)

    def __iter__(self):
        self.__nextindex = 0
        return self

    def __add__(self, other):
        return self.__class__(self.cards + other.cards)

    def __next__(self):
        c = self.cards[self.__nextindex]
        self.__nextindex += 1
        if self.__nextindex == len(self.cards):
            raise StopIteration
        return c

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.cards[item]
        else:
            # item = slice
            return self.cards[item.start:item.stop:item.step]

    def show(self):
        deck_str = f"deck[{len(self.cards)}]:"
        for card in self.cards:
            deck_str += card.to_str()
        return deck_str

    def draw(self, x):
        hand = []
        for _ in range(x):
            card = self.cards.pop(0)
            hand.append(card)
        return self.__class__(hand)

    def shuffle(self):
        random.shuffle(self.cards)



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
    print("#########" * 2, "NEW_TURN")
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
        print("Dealer Cards: ", dealer_cards)
        if dealer_cards.calculate_score() >= 17:
            break
        if dealer_cards == 21:
            dealer_wins = True
        ...  # Смотри подробные правила добора дилера в задании
    print("Dealer: ", dealer_cards)

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
