# Find the factorial of a given number

num = int(input("Please enter number: "))
fac_sum = 1
for i in range(1, num + 1):
    fac_sum *= i 
    
print(f"{num} Factorail is : {fac_sum}")