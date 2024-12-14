# Create a student class and initialize it with name and rollno. Make methods to: 
# Display : It should diplay all information of the student.
# SetAge: It should assign age to student.
# SetMarks: It shoud assign marks to the student.


class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.age = None
        self.mraks = None

    def Display(self):
        print("Student infromation: ")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def SetAge(self, age):
        self.age = age

    def SetMarks(self, marks):
        self.marks = marks



stu = Student("Arfaj", 65)
stu.SetAge(21)
stu.SetMarks(1365)
stu.Display()


        