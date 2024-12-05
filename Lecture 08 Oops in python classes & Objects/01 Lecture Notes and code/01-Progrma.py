# OOPS in python
# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming.


class student: # Create class

    college = "Kirandevi saraf insttitute of complete learning." # Class variable
    name = "ksil" # Class variable 
    def __init__(self,name, age): # Constructor and it has prameter 
        self.name = name  # Instance variable  obje variable > class variable se jyada rahgi
        self.age = age    # Instance variable
        
s1 = student("Arfaj", 23) # Create object and give argument
print(s1.name, s1.age)

s1 = student("Haris", 34) # Cretae 2nd object 
print(s1.name, s1.age)

print(student.college)
print(student.name)



# Methods
# Methode are function that belongs to objects.

class student: # Create class

    college = "Kirandevi saraf insttitute of complete learning." # Class variable
    name = "ksil" # Class variable 
    def __init__(self,name, age): # Constructor and it has prameter 
        self.name = name  # Instance variable  obje variable > class variable se jyada rahgi
        self.age = age    # Instance variable

    
    def hello(self):
        print(f"Hello hii!, {self.name} Welcome to {self.college}({student.name}) college")
    def getage(self):
        print(f"{self.name} Your age is {self.age}")
        
s1 = student("Arfaj", 23) # Create object and give argument
print(s1.name, s1.age)
s1.hello()
s1.getage()





