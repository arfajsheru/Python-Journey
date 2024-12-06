#  15)Counting Digits: Ek number me kitne digits hain, ye count karo bina len() function ke.


def counting_digit(num):
    if num == 0:
        return 1  # 0 ke liye ek digit hoga
    
    count = 0
    num = abs(num)
    
    while num > 0:
        count = count + 1
        num //= 10
    return count
num = int(input("Please enter your number: "))
result = counting_digit(num)
print(result)