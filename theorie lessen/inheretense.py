#als je gewoon classes gebruikt en verschilende classess hebt zal er veel repetitie zijn, overerving helpt hiertegen
#in plaats van onder de init altijd hetzelfde te doen moet dit maar een keer gebeuren.
class Animal:
    def __init__(self, name, weigth):
        self.name = name
        self.weigth = weigth
    def print_information(self):
        print(self.name, self.weigth)
class Dog(Animal):
    pass

class Cat(Animal):   
    pass

d = Dog("Lassy", 15)
d.print_information()
