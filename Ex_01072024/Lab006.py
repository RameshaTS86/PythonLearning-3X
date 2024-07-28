#Ploymorphisam - Polymorphisam allows objects of different
# classes to be treated as objects of a common superclass
#01. Method Overloading - Doesn't Support by Python
#02. Method Overriding

class Shape:
    def area(self):
        print('Area of Class')

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self): #overrideded the method
        super().area()
        print('Area of Rectangle : ',self.length*self.width)

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self): #overrideded the method
        print('Area of Circle : ',3.14*self.radius*self.radius)


cir = Circle(10)
cir.area()

rect = Rectangle(10,10)
rect.area()