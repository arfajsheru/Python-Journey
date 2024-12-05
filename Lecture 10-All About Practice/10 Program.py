# Reverse a integer number

num = int(input("Please enter number: "))
rev_num = 0

while num != 0:
    reminder = num % 10
    rev_num = (rev_num * 10) + reminder
    num = num // 10

print(f"The {num} Reverse number is: {rev_num}")
