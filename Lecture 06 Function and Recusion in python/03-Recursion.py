# RECURSION
# When a function calles iteself repeatedly.


# def show(n):
#     if(n == 0): # Base case
#         return
#     print(n, end="\t")
#     show(n-1)

# show(1000)


# find factorial using recursion 

num = int(input("Enter your number: "))
def fact(num):
    if(num == 0 or num == 1):
        return 1
    else: 
        return num * fact(num-1)

factorial = fact(num)
print(f"{num} factorial is : {factorial}")