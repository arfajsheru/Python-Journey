#  1)Prime Factorization: Ek number ke saare prime factors find karne ka program likho.
# Prime Factors wo factors hote hain jo sirf prime numbers hote hain.

def Prime_Factors(n):
    factore = []
    divisor = 2

    while n > 1: # 36 > 1 = yes, 18 > 1 = yes, 9 > 1 = yes, 3 > 1 = yes, 0 > 1 = no,
        while n % divisor == 0: # 36 % 2 == 0 -> 18, 18 % 2 == 0 -> 9 , 9 % 2 == 0 -> no , 9 % 3 == 0 -> 3, 3 % 3 == 0
            factore.append(divisor) # [2,2,3,3]
            n //= divisor # 36 // 2 = 18, 18 // 2 = 9, 9 // 3 = 3
        divisor += 1 #  2 += 1 = 3, 3 += 1 = 4, 
    return factore
num = int(input("Enter a number: "))
print(f"Prime factors of {num} are: {Prime_Factors(num)}")

