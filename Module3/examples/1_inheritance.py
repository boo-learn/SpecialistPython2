class SuperStr(str):
    def is_repetance(self, s):
        if self.replace(s, "") == "":
            return True
        else:
            return False
    def is_palindrom(self):
        s = self.lower()
        if s == s[::-1]:
            return True
        else:
            return False
        

s = SuperStr("ewew")
print(s.is_repetance("ew"))
print(s.is_palindrom())
