class SuperStr(str):
    def is_repeatance(self, s):
        if len(self):
            if s in self:
                return True
        return False

    def is_palindrome(self):
        return True if self == self[::-1] else False

print(SuperStr('abcdecabc').is_repeatance('abc'))
print(SuperStr('abca').is_palindrome())

