# Abstraction 
# Hiding the implementation details of a class and only showing the essential features to the user.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius 


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width 

    def perimeter(self):
        return 2 * (self.length + self.width)  
    

circle = Circle(5)
rectangle = Rectangle(6,7)


circle = Circle(5)  # Circle ka object banaya
print(f"Circle Area: {circle.area()}")  # Circle ka area calculate kiya
print(f"Circle Perimeter: {circle.perimeter()}")  # Circle ka perimeter calculate kiya

rectangle = Rectangle(4, 6)  # Rectangle ka object banaya
print(f"Rectangle Area: {rectangle.area()}")  # Rectangle ka area calculate kiya
print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Rectangle ka perimeter calculate kiya


# abstraction ak concept he jo complex detail ko hide karta he or essntial features ko expose karta he.pythone abatraction ko achive karne ke liye abstract method or abstract class ka use karte he

# Abstract class ka ham object nahi bana sakte he. Isme abstract methode hote he but uska immplemntation dusri subclass me hota he 

# Abstarct method vo abstract class me declare hot he but uska immplementation subclass me hota he

# Abstract method hamne banaya or hamne uska immplementation subclass me nahi diya to error aayega

