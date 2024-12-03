# Let's Practice with shradha didi

# 1) Print number from 1 to 100 using while loop

i = 1
while i <= 100:
    print(i)
    i += 1


# 2) Print number from 100 to 1 using while loop

i = 100 
while i >= 1:
    print(i)
    i -= 1


# 3) Print the multiplication table of a number n.

num = int(input("Enter your print table number 1 to : "))
i = 1
while i <= num: 
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i * j}") 
        j += 1
    i += 1
    print()


# 4)Print the elements of the following list using a loop:

my_list = [1,4,9,16,25,36,49,64,81,100]

i = 1
while i < len(my_list):
    print(f"{i}: {my_list[i]}")
    i += 1



# 5) Search for a number x in this tupe using loop: 

num = int(input("Enter your find number: "))
my_list = [1,1,1,1,1,4,9,16,25,36,49,64,81,100]
found = False
count = 0
i = 1
while i < len(my_list): 
    if my_list[i] == num:
        found = True 
        count += 1
    i += 1

if found:
    print(f"{num} is availabe in the list {count} times")
else: 
    print(f"{num} is not available in the list")