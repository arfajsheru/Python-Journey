# Write a python program to demonstrate simple inheritance 


class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} Makes sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} Barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meows.")

animal = Animal("Some Animal")
dog = Dog("Buddy")
cat = Cat("Wishkers")

animal.speak()
dog.speak()
cat.speak()

    