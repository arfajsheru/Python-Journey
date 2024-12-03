# Let's Practice with shradha didi

# 1) Print the element of the following list using a loop:
'''
my_list = [1,4,9,25,36,49,64,81,100]
for i in my_list:
    print(i)
'''

# 2) Search for a number x in this tuple using loop
'''
num = int(input("Enter your find number: "))
for i in my_list: 
    if(my_list[i] == num):
        print(f"{my_list[i]} is availabe in list")
        break
'''

# 3) Print number from 1 to 100

'''
for i in range(0,101):
    print(i, end="\t")
'''

'''
# 4) Print numbers from 100 to 1.
for i in range(100,0,-1):
    print(i, end="\t")
''' 

# 4) Print the multiplication table of a number n.
'''
num = int(input("Please enter your multiplication table number: "))
for i in range (1, 11):
    print(f"{num} X {i} = {num * i}")
'''


# 5) Write a program to find the sum of first n natural number using while loop.
'''
num = int(input("Enter your number : "))

i = 0
sum = 0
while i <= num: 
    sum = sum + i
    i += 1

print(f"Sum of n natural number: {sum}")
'''

# 6) Writea a program to find the factorial fo firts n numbers using for loop.
num = int(input("Enter your number: "))
fact_sum = 1
for i in range(1,num+1):
    fact_sum *= i
print(f"Factorial of {num} is: {fact_sum}")



