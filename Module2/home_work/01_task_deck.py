# Колода карт


### Задание

#Разработать класс для “колоды игральных карт”, который в дальнейшем будет использоваться для карточных консольных мини-игр.


### Колода

#Колода состоит из 52 карт.

#Значения карт: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

#Масти карт: ♥ ♦ ♣ ♠

#Говоря “берем карту сверху колоды” подразумеваем получение карты с начала списка колоды.


#### Конструктор колоды

#При создании новой колоды все карты должны находиться в отсортированном порядке - сначала идут все червы от 2-ки до туза, затем буби, крести и пики.


#### Методы колоды

#*   метод **.shuffle**() - перемешивает колоду, располагая карты в случайном порядке.
#*   методы .**draw**(x) - возвращает x первых карт из колоды в виде списка, эти карты убираются из колоды.
#*   метод .**show**() - отображает все карты колоды в формате: \
#deck[12]: 3♥, 4♦, A♣, … \
#где 12 - текущее кол-во карт в колоде.


### Карты

#Карты в колоде тоже должны являться объектами - экземплярами класса Card


#### Конструктор карты

#При создании конструктор карты принимает: значение карты и ее масть. \
#**Примечание:**

#Diamonds    Бубны
#Hearts	    Червы
#Spades	    Пики
#Clubs       Трефы


#### Методы карты

#*   .**to_str**() возвращает строковое представление карты в виде строки, формата:4♦
#*   .**equal_suit**(card) - проверяет, одинаковые ли масти у карт \
#Пример: \
#card1.more(card2) → **True**, при card1(J♦) card2(10♦).
#*   .**more**(card) - возвращает True, если карта у которой вызван метод больше, чем карта которую передали в качестве параметра. \
#**Пример**:  \
#card1.more(card2) → **True**, при card1(J♦) card2(10♦). Валет больше(старше) 10-ки \
#card1.more(card2) → **False**, при card1(4♦) card2(10♦). 4-ка не старше 10-ки
#*   .**less**(card) - проверяет является ли карта младше, чем карта в параметре
##### Нюансы сравнения карт

#Если у карты больше(старше) значение, то она больше(старше). При равенстве значений, сравниваем масти. Старшинство мастей определяем следующее: ♥>♦>♣>♠
##### Вывод иконок карт в консоль

#Пример вывода иконок в консоль:

#print('\u2661', '\u2665') #Hearts	    Червы
#print('\u2662', '\u2666') Diamonds    Бубны
#print('\u2667', '\u2663') #Clubs       Трефы
#print('\u2664', '\u2660') #Spades	    Пики

#\uxxxx - юникод символ. Полный список всех юникод символов можно взять [тут](https://unicode-table.com/ru/#basic-latin).

#Юникод символы мастей игральных карт [тут](https://unicode-table.com/ru/search/?q=%D0%BC%D0%B0%D1%81%D1%82%D0%B8).

SPADES_TYPE = "spades"
HEARTS_TYPE = "hearts"
CLUBS_TYPE = "clubs"
DIAMONDS_TYPE = "diamonds"

class Card:
    types = {
        "diamonds": '\u2666',
        "hearts": '\u2665',
        "spades": '\u2660',
        "clubs": '\u2663',
    }
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f"{self.value}{Card.types[self.type]}"

    def equal_suit(self,card2):
        return self.type==card2.type

    def more(self,card2):
        ty1=['hearts', 'diamonds', 'clubs', 'spades']
        if self.value==card2.value:
            return ty1.index(self.type)<ty1.index(card2.type)
        else:
            return self.value>card2.value

    def less(self,card2):
        ty1=['hearts', 'diamonds', 'clubs', 'spades']
        if self.value==card2.value:
            return ty1.index(self.type)>ty1.index(card2.type)
        else:
            return self.value<card2.value

class Deck:

    def __init__(self):
        self.cards = []


        for type in [HEARTS_TYPE, DIAMONDS_TYPE, CLUBS_TYPE, SPADES_TYPE]:
            for val in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                card = Card(val, type)
                self.cards.append(card)

    def show(self):
        str = f"desk[{len(self.cards)}: ]"
        need_separator = False

        for card in self.cards:
            if need_separator:
                str += ", "
            str += card.to_str()
            need_separator = True

        return str

    def draw(self, x):
        draw_cards=Hand(self.cards[0:x])
        del self.cards[0:x]
        return draw_cards

    def shuffle(self):
        from random import shuffle
        return shuffle(self.cards)

class Hand:
    def __init__(self,deck):
        self.hand=deck

    def show_hand(self):
        str = f"on_hand[{len(self.hand)}: ]"
        need_separator = False

        for card in self.hand:
            if need_separator:
                str += ", "
            str += card.to_str()
            need_separator = True

        return str


card1 = Card(2, 'hearts')
card2= Card(3,'hearts')
card3=Card(2,'diamonds')
card4=Card('J','diamonds')
card5=Card('Q','clubs')
card6=Card('Q','hearts')


print(card1.to_str())

deck = Deck()

print(deck.show())

print(card1.equal_suit(card2))
print(card1.more(card2))
print(card5.more(card4))
print(card6.more(card5))
print(card5.less(card6))

deck.shuffle()
print(deck.show())

deck1=deck.draw(5)

print(type(deck))
print(type(deck1))

print(deck.show())
print(deck1.show_hand())
# deck.shuffle()
# print(deck.show())
