# Print the following pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

num = int(input("Please enter your number: "))

for i in range(num, 0, -1):  # Outer loop from num down to 1
    for j in range(i, 0, -1):  # Inner loop prints from i down to 1
        print(j, end=" ")
    print()   


