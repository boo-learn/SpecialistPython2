class Myfraction:
    def __init__(self, str):
        regex_dilimiter = r'[/ ]+'
        templist = re.split(regex_dilimiter, str) # список list строк str
        self.integerpart = templist[0]
        self.numerator   = templist[1]
        self.denominator = templist[2]
