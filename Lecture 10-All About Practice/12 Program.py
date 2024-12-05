# Calculate the cube of all numbers from 1 to a given number

num = int(input("Please enter number: "))


for i in range(1, num + 1):
    print(f"Current Number is :{i} and the cube is {i * i * i}")