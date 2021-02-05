import random
# from classes.Card import Card


class Deck:
    # @staticmethod
    def create_points(self):
        d1 = {value: int(value) for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']}
        d2 = {value: 10 for value in ['J', 'Q', 'K']}
        d3 = {'A': 11}
        all_cards = dict(**d1, **d2, **d3)
        return all_cards

    points = create_points(0)

    def __init__(self):
        self.cards = []
        self.__next__index__card = 0
        for type in [Card.CLUBS, Card.SPADES, Card.HEARTS, Card.DIAMONDS]:
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(value, type))

    def show(self):
        deck_str = f"deck[{len(self.cards)}]:"
        for card in self.cards:
            deck_str += card.to_str()
        return deck_str

    def __repr__(self):
        deck_str = f"deck[{len(self.cards)}]:"
        for card in self.cards:
            deck_str += card.to_str()
        return deck_str

    def draw(self, x):
        hand = []
        for _ in range(x):
            card = self.cards.pop(0)
            hand.append(card)
        return hand

    def shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self, item):
        if isinstance(item, slice):
            # print(slice.start)
            # print(slice.stop)
            # print(slice.step)
            return self.cards[item]

        return self.cards[item]

    def __iter__(self):
        self.__next__index__card = 0
        return self

    def __next__(self):
        try:
            card = self.cards[self.__next__index__card]
        except IndexError:
            raise StopIteration
        self.__next__index__card += 1
        return card

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
        if Card.values.index(self.value) == Card.values.index(card.value):
            return Card.types.index(self.type) > Card.types.index(card.type)
        return Card.values.index(self.value) > Card.values.index(card.value)

    def __gt__(self, card):
        if Card.values.index(self.value) == Card.values.index(card.value):
            return Card.types.index(self.type) > Card.types.index(card.type)
        return Card.values.index(self.value) > Card.values.index(card.value)

    def __lt__(self, other):
        pass

    def less(self, card):
        pass

    @property
    def point(self):
        # from classes.Deck import Deck
        return Deck.points[self.value]


def summ(cards):
    sum_points = 0
    for card in cards:
        sum_points += card.point
    if sum_points > 21:
        sum_points = 0
        for card in cards:
            if card.value == 'A':
                sum_points += 1
            else:
                sum_points += card.point

    return sum_points

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

deck = Deck()
# deck.shuffle()
# hand = [Card('A', Card.HEARTS),  Card('K', Card.HEARTS)]
# print(hand)
# print(summ(hand))
while True:
    print('Ход игрока')
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    deck.shuffle()
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(f"Карты игрока: {player_cards}")
    print(f"Карты диллера: {dealer_cards}")
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    print(f'Очки игрока: {summ(player_cards)}')
    blackjack = True if summ(player_cards) == 21 else False
    if blackjack:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        # Заканчиваем игру
        break
    else:
        # Если нет блэкджека, то
        while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
            player_choice = input("еще/достаточно: ")
            if player_choice.lower() == "еще" or player_choice.lower() == "ещё":
                # Раздаем еще одну карту
                player_cards+=deck.draw(1)
                print(f"Карты игрока: {player_cards}")
                print(f'Очки игрока: {summ(player_cards)}')
                # Если перебор (>21), заканчиваем добор
                if summ(player_cards)>21:
                    print('много')
                    print(f'В пользу казино списано: {rate_value}')
                    print(f'Остаток игрока: {player_money}')
                    break
                blackjack = True if summ(player_cards) == 21 else False
                if blackjack:
                    # Выплачиваем выигрышь 3 и 2
                    player_money += rate_value * 1.5
                    print("Black Jack!!! Игрок победил")
                    # Заканчиваем игру
                    break
            if player_choice.lower() == "достаточно":
                # Заканчиваем добирать карты
                break


    # Если у игрока не 21(блэкджек) и нет перебора, то
    print('Ход диллера')
    while True:  # дилер начинает набирать карты.
        ...  # Смотри подробные правила добора дилера в задании
        dealer_cards += deck.draw(1)
        print(f"Карты диллера: {dealer_cards}")
        print(f'Очки диллера: {summ(dealer_cards)}')
        blackjack = True if summ(dealer_cards) == 21 else False
        if blackjack:
            # Выплачиваем выигрышь 3 и 2
            player_money -= rate_value
            print("Black Jack!!! Игрок проиграл")
            print(f'В пользу казино списано: {rate_value}')
            print(f'Остаток игрока: {player_money}')
            # Заканчиваем игру
            break
        else:
            

        break
    break
    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    # Если у игрока не 21(блэкджек) и нет перебора, то
    while True:  # дилер начинает набирать карты.
        ...  # Смотри подробные правила добора дилера в задании

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
