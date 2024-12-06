# 5)Perfect Number: Ek number check karo ki wo perfect number hai ya nahi (sum of its divisors is equal to the number).

def is_perfect_number(n):
    divisior_sum = 0 
    for i in range(1,num):
        if(num % i == 0):
            print(i)
            divisior_sum += i

    if divisior_sum == n:
        return True
    else:
        return False

num = int(input("Please enter your number: "))

if is_perfect_number(num):
    print(f"The {num} is Perfect number")
else:
    print(f"The {num} is not Perfect number")
