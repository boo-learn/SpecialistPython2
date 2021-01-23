class Fraction:
    def __init__(self, fr):
        self.int = fr[:fr.find(' ')]
        self.numerator = fr[fr.find(' ') + 1:fr.find('/')]
        self.denominator = fr[fr.find('/') + 1:]

        
        ## без целой части пока не работает
