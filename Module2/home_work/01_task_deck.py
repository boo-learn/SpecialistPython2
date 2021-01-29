class SuperStr(str):

    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        n = len(self) // (len(s) or 1)
        return self == n * s

    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]


mystr = SuperStr('КаЗак')
print(mystr)
print(mystr.is_repeatance('за'))
print(mystr.is_palindrom())
print('------------------')

mystr = SuperStr('казак')
print(mystr)
print(mystr.is_repeatance('за'))
print(mystr.is_palindrom())
print('------------------')

mystr = SuperStr('Ляляля')
print(mystr)
print(mystr.is_repeatance('ля'))
print(mystr.is_palindrom())
print('------------------')

mystr = SuperStr('ляляля')
print(mystr)
print(mystr.is_repeatance('ля'))
print(mystr.is_palindrom())
print('------------------')

mystr = SuperStr('')
print(mystr)
print(mystr.is_repeatance('ля'))
print(mystr.is_palindrom())
print('------------------')
