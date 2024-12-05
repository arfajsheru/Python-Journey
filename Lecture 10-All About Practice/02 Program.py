# Calculate sum of all numbers from 1 to a given number

num = int(input("Please enter your number: "))
sum = 0
for i in range(0, num + 1):
    print(i)
    sum = sum + i
print(f"Sum of all number 1 to {num}: {sum}")