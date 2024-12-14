# Write a python function to calculate the factorail of a number(a non-nagetive integer)

def Factorail(num):
    if num < 0:
        return "Factorial is not define for nagative numbers"
    if num == 0 and num == 1:
        return 1
    

    result = 1

    for i in range(1, num +1):
        result = result * i
    
    return result

number = int(input("Enter your number: "))
print(f"The factor of {number} is {Factorail(number)}")
        