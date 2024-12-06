#  11)Armstrong Number: Ek number check karo ki Armstrong number hai ya nahi.

def is_armstrong_number(num):

    num_str = str(num)
    num_digit = len(num_str)
    arm_sum = 0

    for digit in num_str:
        arm_sum += int(digit) ** num_digit
    return arm_sum == num

number = int(input("Please entet your number: "))
if is_armstrong_number(number):
    print(f"{number} is armstrong number")
else: 
    print(f"{number} is not armstrong number")

