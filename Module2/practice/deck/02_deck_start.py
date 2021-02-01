class Deck:
    def __init__(self):
        self.cards = []
        for c in Card.HEARTS, Card.CLUBS, Card.SPADES, Card.DIAMONDS:
            for v in '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A':
                self.cards.append(Card(v, c))
