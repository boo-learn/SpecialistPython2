    def more(self,card2):
        ty1 = ['hearts', 'diamonds', 'clubs', 'spades']
        values=[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        if self.value == card2.value:
            return ty1.index(self.type) < ty1.index(card2.type)
        else:
            return values.index(self.value) > values.index(card2.value)
