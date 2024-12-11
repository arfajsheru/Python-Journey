# 14) Create a program in python that asks the user for a number and then prints out a list of all the divisors fo that number.


def divisor(n):
    mylist = []
    for i in range(1,n+1):
        if(n % i == 0):
            mylist.append(i)
    return mylist


num  = int(input("Enter your number: "))
result = divisor(num)
print(result)
