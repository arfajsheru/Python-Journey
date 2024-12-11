#  13)Palindrome Number: Ek number palindrome hai ya nahi, ye check ka

def is_palindrome(num):
    if num < 0:
        return False
    
    reverse_no = 0
    while num > 0:
        digit = num % 10
        reverse_no = reverse_no * 10 + digit
        num //= 10

    return reverse_no

number = int(input("Please enter you number: "))
if(is_palindrome(number) == number):
    print(f"{number} is palindrome number")
else:
    print(f"{number} is not palindrome number")
