class BJ_Card(Card):
    def getvalue(self: Card, hand_score):
        if self.value in {"K", "Q", "J"}:
            return 10
        if self.value == "A":
            return 1 if hand_score > 10 else 11
        return int(self.value)
