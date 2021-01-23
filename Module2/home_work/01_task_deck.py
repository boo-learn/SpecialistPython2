import random

from collections import Counter


values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
types = {
    'hearts': {'unicode': '\u2665', 'priority': 3},
    'diamonds':  {'unicode': '\u2666', 'priority': 2},
    'clubs':  {'unicode': '\u2663', 'priority': 1},
    'spades':  {'unicode': '\u2660', 'priority': 0}
}


class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return self.to_str

    @property
    def to_str(self):
        return f"{self.value}{types[self.type]['unicode']}"

    def equal_suit(self, other):
        if self.type == other.type:
            return True
        return False

    def more(self, other):
        if values.index(self.value) > values.index(other.value) \
                and values.index(self.value) != values.index(other.value):
            return True
        elif values.index(self.value) == values.index(other.value) \
                and types[self.type]['priority'] > types[other.type]['priority'] \
                and types[self.type]['priority'] != types[other.type]['priority']:
            return True
        return False

    def less(self, other):
        return not self.more(other)


class Deck:
    def __init__(self):
        self.cards = []

        for type in types:
            for value in values:
                card = Card(value, type)
                self.cards.append(card)

    def show(self):
        return print(f'deck[{len(self.cards)}]: {[card for card in self.cards]}')

    def draw(self, x):
        drawed = []
        for i in range(x):
            drawed.append(self.cards.pop(i))
        return drawed

    def shuffle(self):
        return random.shuffle(self.cards)


def test1():
    print(f'\nЗадание-1')
    print(f'Условия:')
    print(f'Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху. Сравните эти карты и выведите сообщение формата: “карта Adiamonds больше Jclubs”')
    print(f'Ответ:')
    deck = Deck()
    deck.shuffle()
    hand = deck.draw(2)
    if hand[0].more(hand[1]):
        big = hand[0]
        small = hand[1]
    else:
        big = hand[1]
        small = hand[0]
    print(f'карта {big.value}{big.type} больше {small.value}{small.type}')


def test2():
    print(f'\nЗадание-2')
    print(f'Условия:')
    print(f'Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?')
    print(f'Ответ:')
    deck = Deck()
    deck.shuffle()
    hand = deck.draw(10)
    hand_types = [i.type for i in hand]
    c = Counter(hand_types)
    hand_types_max_count = ', '.join([k for k, v in c.items() if v == max(c.values())])
    print(f'Среди вытянутых карт больше всего оказалось {hand_types_max_count}')


def test3():
    print(f'\nЗадание-3')
    print(f'Условия:')
    print(f'Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху. Снова перемешайте колоду и вытяните еще одну. Если вторая карта меньше первой, повторите “перемешать + вытянуть”, до тех пор, пока не вытяните карту больше предыдущей карты. В качестве результата выведи все вытягиваемые карты в консоль.')
    print(f'Ответ:')
    deck = Deck()
    deck.shuffle()
    drawed = []
    card1 = deck.draw(1)[0]
    drawed.append(card1)
    while len(deck.cards) > 0:
        deck.shuffle()
        card2 = deck.draw(1)[0]
        drawed.append(card2)
        if card2.less(card1):
            card1 = card2
            continue
        else:
            break
    return print(drawed)


def test4():
    print(f'\nЗадание-4')
    print(f'Условия:')
    print(f'''Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается с 6-ки). Перемешайте их.
Вытягивайте карты парами - одну из первой колоды, вторую из второй.
Если карта из первой колоды окажется больше(старше), то записываем 1:0 (условно начисляем победное очко первой колоде), если карты одинаковые, то не учитываем очко никуда.
Выведите итоговый счет, сравнив попарно все карты в колодах.''')
    print(f'Ответ:')
    deck1 = Deck()
    deck1.cards = [c for c in deck1.cards if values.index(c.value) > 3]
    deck1.shuffle()
    deck2 = Deck()
    deck2.cards = [c for c in deck2.cards if values.index(c.value) > 3]
    deck2.shuffle()
    deck1.count = 0
    deck2.count = 0
    while len(deck2.cards) > 0:
        hand = [deck1.draw(1)[0], deck2.draw(1)[0]]
        if hand[0].more(hand[1]):
            deck1.count += 1
        else:
            deck2.count += 1
    return print(f'{deck1.count}:{deck2.count}')


def test5():
    print(f'\nЗадание-5 “Дурак без козырей”')
    print(f'Условия:')
    print(f'''Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”.

    Создайте колоду из 52 карт. Перемешайте ее.
    Первый игрок берет сверху 6 карт
    Второй игрок берет сверху 6 карт.
    Игрок-1 ходит:
        игрок-1 выкладывает самую маленькую карту по значению
        игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
        Если игрок-2 не может побить карту, то он проигрывает.
        Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
    Выведите в консоль максимально наглядную визуализацию данного игрового хода.
''')
    print(f'Ответ:')
    table = []
    deck = Deck()
    deck.shuffle()
    player1 = deck.draw(6)
    player2 = deck.draw(6)
    player1_min_card = player1[0]
    print(f'Рука игрока-1: {[i for i in player1]}')
    for c in player1:
        if c.less(player1_min_card):
            player1_min_card = c
    table.append(player1.pop(player1.index(player1_min_card)))
    print(f'Игрок-1 кладет карту {player1_min_card}')
    while len(player2) > 0:
        print(f'Рука игрока-2: {[i for i in player2]}')
        player2_hand_types = [types[i.type] for i in player2]
        player2_list_to_defend = [c for c in player2 if c.type == table[-1].type and values.index(c.value) > values.index(table[-1].value)]
        if not len(player2_list_to_defend):
            return print(f'Игроку-2 нечем бить. Игрок-1 выиграл.')
        player2_min_card = player2_list_to_defend[0]
        for c in player2_list_to_defend:
            if c.less(player2_min_card):
                player2_min_card = c
        table.append(player2.pop(player2.index(player2_min_card)))
        print(f'Игрок-2 отбивается картой {player2_min_card}')
        print(f'На столе {[c for c in table]}')
        table_values = [i.value for i in table]
        player1_can_add = []
        for c in player1:
            if c.value in table_values:
                player1_can_add.append(c)
        if not len(player1_can_add):
            return print(f'Игроку-1 нечего подкидывать')
        player1_can_add_min_card = player1_can_add[0]
        for c in player1_can_add:
            if c.less(player1_can_add_min_card):
                player1_can_add_min_card = c
        print(f'Рука игрока-1: {[i for i in player1]}')
        table.append(player1.pop(player1.index(player1_can_add_min_card)))
        print(f'Игрок-1 подкидывает {player1_can_add_min_card}')
        print(f'На столе {[c for c in table]}')


def test6():
    print(f'\nЗадание-6')
    print(f'Условия:')
    print(f'Создайте две колоды по 52 карты. Перемешайте их вместе - в итоге получится одна колода из 104 карт. Выбросите/вытяните половину карт. Узнайте, какой/каких мастей в колоде осталось больше всего?')
    print(f'Ответ:')
    deck = Deck()
    deck2 = Deck()
    deck.cards += deck2.cards
    deck.shuffle()
    deck.cards = deck.cards[int(len(deck.cards)/2):]

    deck_types = [i.type for i in deck.cards]
    c = Counter(deck_types)
    deck_types_max_count = ', '.join([k for k, v in c.items() if v == max(c.values())])
    return print(f'Больше всего в колоде осталось {deck_types_max_count}')


def run_tests():
    print(f'\nВыполнение заданий')
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()


def main():
    run_tests()


if __name__ == '__main__':
    main()

