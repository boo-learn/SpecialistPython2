class Super_Str(str):
    def is_palindrom(self,st1):
        return self.lower()==st1.lower()[::-1]

    def is_repiatance (self,str1):
        if str(type (str1))!="<class 'str'>": #при любом типе переменной ошибки не будет
            return False
        else:
            self=self.lower()
            str1=str1.lower()
            return len(self.split(str1))==self.split(str1).count('')

st1=Super_Str('asdfghjkl')
st2=Super_Str('lkjhgfdsa')
st3=Super_Str('LKJhgFDSA')
st4=Super_Str('LKJhgFsSA')
st5=Super_Str('dsadsadsadsa')
st6=Super_Str('dsadsafdsadsafdsa')

print(st5.is_repiatance('DsA'))
print(st6.is_repiatance('DsA'))
print(st5.is_repiatance(1.1))
print(st1.is_palindrom(st2))
print(st1.is_palindrom(st3))
print(st1.is_palindrom(st4))
