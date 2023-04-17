class Point:
    def __init__(self, x, y):
        assert x>=0, "error: x can't be negative!"
        #hier geen underscores om de waarde van point altijd na te gaan: voor de rest laat die underscores wel.
        #De underscore moet staan bij waardes, zoals onder property maar hier wordt de setter opgeroepen.
        self.x = x
        self.y = y
    #een get functie
    @property
    def x(self):
        return self.__x
    #Als hier boven geen underscore staat zou er een oneindige lus komen (naam moet anders zijn en variable moet niet direct aangeroepen of aan gepast worden)

    @property
    def y(self):
        return self.__y
    
    #een set functie
    @x.setter
    def x(self, value):
        if value<0:
            raise ValueError("X cannnot be negative!")
        else:
            self.__x = value
    @y.setter
    def y(self, value):
        if value<0:
            raise ValueError("Y cannnot be negative!")
        else:
            self.__y = value


    def __add__(self, other):
        return Point(
            self.x +other.x,
            self.y+other.y
        )



p1= Point(10, 5)
p2= Point(5, 3)
# zo zou het eruit zien zonder de underscore naast zelf
#p1.add(p1, p2)
#nu is add gewoon +

p1+p2
print(p1.x)
