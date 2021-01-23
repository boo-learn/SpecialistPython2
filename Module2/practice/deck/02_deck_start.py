import random
import operator

SPADES_TYPE = "spades"
HEARTS_TYPE = "hearts"
CLUBS_TYPE = "clubs"
DIAMONDS_TYPE = "diamonds"

#-------------------------------------------------------------------

class Card:

    TYPES_DICT = {SPADES_TYPE: "♠", HEARTS_TYPE: "♥", CLUBS_TYPE: "♣", DIAMONDS_TYPE: "♦"}
    __VALUE_WEIGHT = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    __TYPES_WEIGHT = {SPADES_TYPE: 1, CLUBS_TYPE: 2,  DIAMONDS_TYPE: 3,HEARTS_TYPE: 4}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        """возвращает строковое представление карты в виде строки, формата:4♦"""
        return f"{self.value}{self.TYPES_DICT[self.type]}"

    def equal_suit(self, card) :
        """проверяет, одинаковые ли масти у карт"""
        return self.type == card.type

    def __type_weight(self):
        #Старшинство мастей определяем следующее: ♥>♦>♣>♠
        return self.__TYPES_WEIGHT[self.type]

    def __value_weight(self):
        return self.__VALUE_WEIGHT[self.value]

    def more(self, card):
        #возвращает True, если карта у которой вызван метод больше, чем карта которую передали в качестве параметра.

        if self.__type_weight() > card.__type_weight() :
            return True

        if self.__type_weight() < card.__type_weight():
            return False

        return self.__value_weight() > card.__value_weight()

    def less(self, card):
        # проверяет является ли карта младше, чем карта в параметре
        if self.__type_weight() < card.__type_weight() :
            return True

        if self.__type_weight() > card.__type_weight():
            return False

        return self.__value_weight() < card.__value_weight()

#-------------------------------------------------------------------

class Deck:
    def __init__(self):
        self.cards = []

        for type in [HEARTS_TYPE,DIAMONDS_TYPE,CLUBS_TYPE,SPADES_TYPE]:
            for val in range(2,11):
                self.cards.append(Card(val, type))

            for val in ["J", "Q", "K", "A"]:
                self.cards.append(Card(val, type))

    def show(self):
        str = f"desk[{len(self.cards)}]: "
        need_separator = False

        for card in self.cards:

            if need_separator:
                str += ", "

            str += f"{card.to_str()}"
            need_separator = True

        return str

    def draw(self, x):
        #методы .draw(x) - возвращает x первых карт из колоды в виде списка, эти карты убираются из колоды.

        r = []
        for cx in range(0,x):
            r.append(self.cards.pop(0))

        return r

    def shuffle(self):
        #метод .shuffle() - перемешивает колоду, располагая карты в случайном порядке.

        new_arr = []

        while len(self.cards) > 0:
            indx = random.randint(0, len(self.cards) - 1)
            new_arr.append(self.cards.pop(indx))

        self.cards = new_arr

#-------------------------------------------------------------------

class SuitCount:
    def __init__(self, type):
        self.type = type
        self.cnt= 0

    def to_str(self):
        return f"{Card.TYPES_DICT[self.type]}={self.cnt}"

#-------------------------------------------------------------------

def task_1() :
    #Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху. Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”
    #Старшинство мастей определяем следующее: ♥>♦>♣>♠

    print("Задание 1")

    deck = Deck()
    deck.shuffle()
    cards = deck.draw(2)

    print(f"Вытащили карты {cards[0].to_str()} и {cards[1].to_str()}")

    if cards[0].more(cards[1]):
        print(f"Карта {cards[0].to_str()} больше {cards[1].to_str()}")
    else:
        print(f"Карта {cards[0].to_str()} меньше {cards[1].to_str()}")

#-------------------------------------------------------------------

def task_2():
    #Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?

    print("Задание 2")

    deck = Deck()
    deck.shuffle()
    cards = deck.draw(10)

    print(f"Вытащили карты: ", end=" ")

    cx = 0
    suit = {}

    for card in cards :
        cx += 1
        end_prn = ", " if cx < len(cards) else " "
        print(card.to_str(), end=end_prn)

        count_item = suit.get(card.type, SuitCount(card.type))
        count_item.cnt += 1
        suit[card.type] = count_item

    print()

    print(f"Количество карт по масти: ", end=" ")

    for count_item in suit.items() :
        print(count_item[1].to_str(), end=" ")

    print()

    sorted_tuples = sorted(suit.values(), key=lambda v:v.cnt, reverse=True)

    max_count = []

    for item in sorted_tuples :
        if len(max_count) == 0:
            max_count.append(item)
            continue

        if max_count[0].cnt > item.cnt:
            continue

        if  max_count[0].cnt < item.cnt :
            max_count.clear()
            max_count.append(item)
            continue

        max_count.append(item)

    print(f"Больше всго карт масти: ", end=" ")

    for count_item in max_count:
        print(count_item.to_str(), end=" ")

    print()




#-----------------------------------------------------

print("-----------------------------------------")
deck = Deck()
print(deck.show())
print("-----------------------------------------")
deck.shuffle()
print(deck.show())
print("-----------------------------------------")
#task_1()
print("-----------------------------------------")
task_2()
print("-----------------------------------------")
