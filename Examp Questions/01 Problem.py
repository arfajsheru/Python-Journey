# Write a python program to check if the enterd number is a prime number.

def is_prime(num):
    if num < 1:
        return False
    
    for i in range(2, num):
        if(num % i == 0):
            return False
  
    return True


number = int(input("Enter your number: "))
if is_prime(number):
    print(f"{number} is prime number")
else:    
    print(f"{number} is not prime number")




