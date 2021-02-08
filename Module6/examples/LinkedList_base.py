# Программа баржа
# Работает нормально, но организована не совсем традиционным способом
# Изначально задается прямо объект баржа с объектами отсеками
# Перемещение груза в отсеках проиходит автоматически циклом приоперациях погрузки и разгрузки
# Можно было оперировать стандартными методами списков
# Здесь как в жизни, бочки перемещаются по очереди
#

class Compartment:
    def __init__(self,carry):
        self.carry=carry
        self.compartment=[]
        for i in range (0,carry):
            self.compartment.append(0)

    def to_str(self):
        out=""
        for i in self.compartment:
            out+= f" [ {i} ] "
        return out

    def can_load(self):
        for i in self.compartment:
            if i==0:
                return True
        return False

    def load_barrel(self,barrel):
        if self.can_load():
            for i in range(-1, -self.carry - 1, -1):
                if self.compartment[i]!=0:
                    self.compartment[i+1]=self.compartment[i]
            self.compartment[0]=barrel
        else:
            raise TypeError("Отсек полон")

    def can_unload(self):
        if self.compartment[0]!=0:
            return True
        return False

    def unload_barrel(self):
        if self.can_unload():
            barrel=self.compartment[0]
            i=0
            for i in range (0,self.carry-1):
                if self.compartment[i]!=0:
                    self.compartment[i]= self.compartment[i+1]
            self.compartment[i + 1]=0
            return barrel
        else:
            raise TypeError("Отсек пуст")





class Barka:
    def __init__(self,holds,carry,max_cargo=2): #
        self.holds=holds
        self.carry=carry
        self.cargo=0
        self.max_cargo=max_cargo
        self.barka=[]
        for i in range (0,holds):
            self.barka.append(Compartment(carry))

    def __str__(self):
        if self.holds>0:
            out=f"Баржа отсеков: {self.holds} емкость каждого {self.carry} максимальный груз: {self.max_cargo}\n"
            n=0
            for i in self.barka:
                out+=f"Отсек № {n} состояние :{i.to_str()}  \n"
                n+=1
            out+=f"Текущая загрузка {self.cargo} Максимальная загрузка {self.max_cargo}"
            return out
        return f"Баржа без отсеков"

    def load (self,hold,fuel):
        if self.cargo==self.max_cargo:
            raise TypeError("Перегрузка, баржа утонет")
        self.barka[hold].load_barrel(fuel)
        self.cargo+=1
        return f" Топливо {fuel} в отсек {hold} успешно погружено"

    def unload (self,hold,fuel):
        fuel_barrel=self.barka[hold].unload_barrel()
        if fuel_barrel==fuel:
            self.cargo-=1
            return f" Заказанное топливо {fuel} из отсека {hold} успешно выгружено"
        else:
            raise TypeError("Топливо выгружено не то")




barka1=Barka(0,2,2)
print(barka1)

barka=Barka(2,3,3)
print(barka)


print(barka.load(0,99))
#print(barka)
print(barka.load(0,20))
#print(barka)
print(barka.load(0,29))
print(barka)



print(barka.unload(0,99))
print(barka.unload(0,20))
#print(barka)
print(barka.unload(0,99))
print(barka)
