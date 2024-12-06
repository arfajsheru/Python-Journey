#  8)Decimal to Binary Conversion: Ek decimal number ko binary me convert karo bina built-in function ke.

def decimal_to_binary(num):
    binary = []
    
    while num > 0:
        reminder = num % 2
        binary.append(str(reminder))
        num //= 2


    binary.reverse()
    return ' '.join(binary)

decimal_number = int(input("Please enter your number: "))
binary_result = decimal_to_binary(decimal_number)

print(f"Binary representation of {decimal_number} is: {binary_result}")