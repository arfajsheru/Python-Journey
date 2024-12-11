#  2)Fibonacci Number Check: Ek program banao jo check kare ki given number Fibonacci series ka part hai ya nahi.
import math
# def generate_fibonacci(n):
#     fib_series= []
#     a , b = 0 ,1
#     for _ in range(n):
#         fib_series.append(a)
#         a, b = b, a + b
#     return fib_series

# term = int(input("Please enter your number: "))
# if term >= 0:
#     result = generate_fibonacci(term)
#     print("Fibonacci series: ", result)
# else:
#     print("Please enter your positive integer number")

# important point
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return (s * s) == x

def is_fibonacci_number(n):

    check1 = 5 * n * n + 4
    check2 = 5 * n * n - 4

    return is_perfect_square(check1) or is_perfect_square(check2)

num = int(input("Please enter your number: "))
if is_fibonacci_number(num):
    print(f"{num} is fibonacci number")
else: 
    print(f"{num} is not fibonacci number")

# Step-by-Step Breakdown
# Step 1: Input the number.

# The program takes a number from the user that needs to be checked.
# Step 2: Check the condition using the function is_fibonacci_number(num).

# If the number satisfies the condition, it will proceed further.
# Step 3: Inside the is_fibonacci_number function:

# Two values are calculated:
# check1 = 5 * n * n + 4
# check2 = 5 * n * n - 4
# Step 4: The return statement is used to evaluate the condition:

# The is_perfect_square function is called for both check1 and check2.
# The or operator checks if either of them returns True.
# Step 5: Inside the is_perfect_square function:

# For the given number x (either check1 or check2), the square root is calculated using math.sqrt(x).
# The square of the square root is computed to verify if it equals the original number x.
# Step 6: The square is checked against the original number using the condition s * s == x.

# If this condition is true, the number is a perfect square.
# Step 7: If the is_perfect_square function returns True, control goes back to the is_fibonacci_number function, which then returns True.

# Step 8: If True is returned:

# The number is confirmed to be part of the Fibonacci series.
# The program prints that the number is a Fibonacci number.
# Step 9 (else case):

# If none of the conditions are satisfied, the number is not part of the Fibonacci series, and the program prints that it is not a Fibonacci number.
