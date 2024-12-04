# 1)Write a python program to check the if a number entered by user is odd or even.
'''
num = int(input("Please enter a number: "))
if(num % 2 == 0):
    print(num, "is even number")
else: 
    print(num, "is odd number")
'''
# Output: Please enter a number: 4
# 4 is even number

# 2)Write a python program to find the greatest of three numbers entered by user.
'''
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter seconde number: "))
num3 = int(input("Please enter third number: "))

if(num1 >= num2 and num1 >= num3):
    print(num1, "is greatest of all numbers")
    if(num1 == num2  and num1 == num3): 
        print("but all numbers are equals")
    elif(num1 == num2):
        print(f"but {num1} and {num2} are equals")
    elif((num1 == num3)): 
        print(f"{num1} and {num3} are equals")
elif(num2 >= num3 and num2 >= num1):
    print(num2, "is greatest of all numbers")
    if(num2 == num1):
        print(f"but {num2} and {num1} are equals")
    elif((num2 == num3)): 
        print(f"{num2} and {num3} are equals")
else:
    print(num3, "is greatest of all numbers")
    if(num3 == num1):
        print(f"but {num3} and {num1} are equals")
    elif((num3 == num2)): 
        print(f"{num3} and {num2} are equals")
'''

# 3)Write a python program to check if a number is multiple of 7 or not

num = int(input("Please enter you number 1... 1000 : "))
if(num % 7 == 0): 
    print("Multiple of 7")
else:
    print("not a multiplie of 7")