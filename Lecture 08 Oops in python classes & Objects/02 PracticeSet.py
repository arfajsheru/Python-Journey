# Let's Practice with shradha didi

# Create student class that takes name & marks of 3 subjects as arguments in constructor Then createa a method to print the average.


class Student:
    
    def __init__(self,sub1,sub2,sub3,name):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.name = name
    
    def average(self):
        sum = self.sub1 + self.sub2 + self.sub3
        return sum / 3
    
    def percentage(self):
        sum = self.sub1 + self.sub2 + self.sub3
        percentage = (sum / 300 ) * 100
        return round(percentage, 2) 


marks1 = int(input("Please enter your first marks: "))
marks2 = int(input("Please enter your second marks: "))
marks3 = int(input("Please enter your third marks: "))
name = (input("Please enter your name: "))

s1 = Student(marks1, marks2, marks3, name)

print(f"Subject one marks:{s1.sub1}\nSubject seconde marks: {s1.sub2} \nSubbject third marks: {s1.sub3}")

print(f"Print the average of three subject: {s1.average()}")
print(f"Percenrage: {s1.percentage()}%")

print(f"Hii {s1.name} your average score is {s1.average()} and percentage is {s1.percentage()}%")