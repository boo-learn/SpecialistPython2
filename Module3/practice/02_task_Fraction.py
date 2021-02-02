    def __mul__(self, other:int):
        return Fraction(f"{self.numerator * other}/{self.denominator}")
