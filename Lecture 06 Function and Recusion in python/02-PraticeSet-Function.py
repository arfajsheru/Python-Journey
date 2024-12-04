# Let's Practice with shradha didi
# 1) Write a pogram to print the length of a list. (list is prameter).
cities = ["Delhi", "Gurgaon","Noida", "Pune", "Mumbai", "Chennai"]
heroes = ["Thor", "Ironman", "Captain america", "Shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


# 2) Write a program to print the elements of a list in a single line.(list is the parameter).
def print_list(list):
    for item in list: 
        print(f"{item} ", end=" ")
    print()
print_list(cities)
print_list(heroes)

# 3) Write a program to find the factorial of n. (n is the prameter)

num = int(input("Enter your factorial number: "))

def factorial(num):
    i = 1
    fac_sum = 1
    for i in range(1,num+1):
        fac_sum *= i
    print(f"{num} factorial is {fac_sum}")

factorial(num)

# 4) Write a program to convert a usd to inr

num = int(input("Enter your usd doller number: "))
def conveter(usd_val):
    inr_val = usd_val * 83
    print(f"{usd_val} USD = {inr_val} INR")


conveter(num)

# 5) Home work practice: Write program create a function tack input from user and check whether the number is odd or even.

num = int(input("Enter your number: "))
def check_number(num):

    if(num % 2 == 0):
       return "Even"
    else: 
       return "Odd"
    

result = check_number(num)
print(result)