# Let's Practice

# 1) Write a program to store following word meanings in a python dictionary:
    # table : "A Piece of furniture", "List of facts & figures"
    # cat: "A small animal"

store = {
    "cat": "A small animal",
    "table": ["A piece of furniture", "list of facts & figures"]
}

# 2) You are fiven a list of subjects for students. Assume one classrooom is required for a subject. How many classrooms are needed by all studentes.
subjects = ["python","java", "c++", "python", "javascript","java", "python", "java", "c++", "c"]

setSubjects = set(subjects)
print(setSubjects)
print(len(setSubjects))

# 3) Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add on by one. Use subject names as key & marks as value.

stu_res = {}
total_marks = 0

for i in range(1,5):
    subjects = input(f"Enter your {i} subjects name: ")
    marks = int(input(f"Enter marks for {subjects} (out of 100): "))
    stu_res[subjects] = marks
    total_marks += marks

print(stu_res)
print(stu_res.keys())


average_marks = total_marks / len(stu_res)
percentage = (total_marks / (len(stu_res) * 100)) * 100


if percentage >= 90:
    feedback = "Excellent"
elif 70 <= percentage < 90:
    feedback = "Good"
elif 50 <= percentage < 70:
    feedback = "Average"
else:
    feedback = "Fail"

# Display results
print("\nStudent Results:")
for subject, marks in stu_res.items():
    print(f"{subject}: {marks} marks")

print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Result: {feedback}")