class Money:
    pass
    # TODO: your code here

    
    ###
    class Money:

    def __init__(self, count_of_roubles,count_of_penny):
        self.count_of_roubles = count_of_roubles
        self.count_of_penny = count_of_penny

    def __add__(self, other_rouble, other_penny):
        if ((self.count_of_penny + other_penny) < 100 ):

            new_rouble = self.count_of_roubles + other_rouble
            new_penny =  self.count_of_penny + other_penny
            print(new_rouble, "руб", new_penny, "коп")
            return new_rouble, new_penny
        else:
            new_rouble = self.count_of_roubles + 1 + other_rouble
            new_penny = self.count_of_penny - 100 + other_penny
            print(new_rouble, "руб", new_penny, "коп")

            return new_rouble, new_penny

    def __truediv__(self, other_rouble, other_penny):
        if (self.count_of_penny > other_penny):
            return self.count_of_roubles + other_rouble, self.count_of_penny - other_penny
        else:
            return self.count_of_roubles - 1 - other_rouble, self.count_of_penny + 100 - other_penny

    def __mul__(self, other):
        return self.count_of_money * other

    def __sub__(self, other):
        return self.count_of_money - other


my_money =  Money(100,10)

my_money.__add__(10,10)
