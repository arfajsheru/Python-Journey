marks = int(input("Enter your marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >=50 and marks < 80):
    grade = "C"
elif(marks < 50):
    grade = "F"
else: 
    print("Invalid marks ")

print("Grade of the student -> ", grade)