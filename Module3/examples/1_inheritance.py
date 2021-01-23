class Drob:
    def __init__(self, string):
        self.celoe = None
        if ' ' in string:
            self.celoe = string.split(' ')[0]
            if self.celoe:
                self.celoe = int(self.celoe)
                self.chislitel = int(string.split(' ')[1].split('/')[0])
                self.znamenatel = int(string.split(' ')[1].split('/')[1])
        else:
            self.chislitel = int(string.split('/')[0])
            self.znamenatel = int(string.split('/')[1])

    def to_float(self):
        if self.celoe:
            return self.celoe + (self.chislitel / self.znamenatel)
        else:
            return self.chislitel / self.znamenatel

    def __add__(self, other):
        return self.to_float() + other.to_float()

a = Drob('2 3/12')
print(a.celoe)
print(a.chislitel)
print(a.znamenatel)
print(a.to_float())
print(a + a)
