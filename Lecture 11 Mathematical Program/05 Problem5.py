#  8)Binary to decimal Conversion: Ek decimal number ko binary me convert karo bina built-in function ke.

def binary_to_decimal(binary):
    decimal = 0
    binary = str(binary)
    length = len(binary)

    
    for i in range(length):
        str_index = int(binary[i])
        power = length - 1 - i
        decimal = decimal + str_index * (2 ** power)
    return decimal


binary_num = input("Please etner your binary number: ")
decimal_result = binary_to_decimal(binary_num)
print(f"The decimal representation of binary {binary_num} is: {decimal_result}")
        
