# Write a Python program to accept the age of n employees and count the number of persons in the following age group:
# (i) 26-35
# (ii) 36-45
# (iii) 46-55
n = int(input("Enter the the number of employess: "))
ages = []
for i in range(1,n+1):
    age = int(input(f"Enter the age of employee {i + 1}: "))
    ages.append(age)
group_26_35 = 0
group_36_45 = 0
group_46_55 = 0
for age in ages: 
    if 26 <= age <= 35:
        group_26_35 += 1
    elif 36 <= age <= 45: 
        group_36_45 += 1
    elif 46 <= age <= 55:
        group_46_55 += 1
print("\n Number of employess in the age groups: ")
print(f"26 to 35: {group_26_35}")
print(f"36 to 45: {group_36_45}")
print(f"46 to 55: {group_46_55}")