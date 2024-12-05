# Print all prime numbers within a range

num1 = int(input("Please enter your start number: "))
num2 = int(input("Please enter your end number: "))

for num in range(num1, num2 + 1):
    if  num > 1: 
        is_Prime = True
        for j in range(2, num):
            if(num % j ==  0):
                is_Prime = False
                break
        if is_Prime:
            print(num, end=" ")
