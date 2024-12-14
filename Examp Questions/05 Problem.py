# Write a python program to calculate the sum of all numbers from 1 to a given number

def given_no_sum(num):
    sum = 0
    for i in range(num+1):
        sum += i

    return sum 
number = int(input("Please enter your number: "))
result = given_no_sum(number)
print(f"Enter your given number is: {result}")
