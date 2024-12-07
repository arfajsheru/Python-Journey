# Write a program to print the sum of digit number input from the user.


def sum_of_digit(num):
    sum = 0
    while num >= 1:
        digit = num % 10
        sum += digit
        num //= 10
    return sum

number = int(input("Please enter your number: ")) 
result = sum_of_digit(number)

print(f"{number} sum of digit is: {result}")
