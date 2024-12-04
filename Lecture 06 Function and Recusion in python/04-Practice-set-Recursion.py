# Let's Practise With shradha didi

# 1) Write a recursive function to calculate the sum of first n natural numbers.
num = int(input("Please enter your number: "))
def natural_sum(num):
    if(num == 0):
        return 0
    return num + natural_sum(num - 1)

result = natural_sum(num)

# output learning: natural_sum(4) → 4 + natural_sum(3)
                                # → 4 + (3 + natural_sum(2))
                                # → 4 + (3 + (2 + natural_sum(1)))
                                # → 4 + (3 + (2 + (1 + natural_sum(0))))
                                # → 4 + 3 + 2 + 1 + 0 = 10

# print(f"sum of natural numbers from 1 to {num}: {result}")

# 2) Write a recursive function to print all elements in a list.

def print_list(list):
    if not list:
        return
    print(list[0],end=" ")

    print_list(list[1: ])

element = []
for i in range(1,5):
    num = int(input(f"Enter your number {i}: "))
    element.append(num)

print_list(element)

# Let's Advance practice

# Normal element print
def print_list(lst, index = 0):
    if(index == len(lst)): # Index reaches and of list
        return
    print(lst[index], end=" ")
    print_list(lst, index + 1) # Recursive call with next index

mylist = []
num = int(input("Enter your mylist length number: "))
for i in range(1, num+1):
    num = int(input(f"Enter your {i} number: "))
    mylist.append(num)

print("Element in the normal list are: ", end=" ")
print_list(mylist)



# Print reverse element
def print_reverse_list(lst, index=0):
    if index == len(lst):
        return
    
    print_reverse_list(lst, index + 1)
    print(lst[index], end=" ")

print("\nElement in the reverse list are: ", end=" ")
print_reverse_list(mylist)



# Sum of element list
def sum_list(lst, index = 0):
    if index == len(lst):
        return 0
    return lst[index] + sum_list(lst , index + 1)
print(f"\nSum of elements: {sum_list(mylist)}", end=" ")



# Find maximum number in list
def find_max(lst, index = 0, max_val = float('-inf')):
    if index == len(lst):
        return max_val
    
    return find_max(lst, index + 1, max(max_val, lst[index]))
print(f"\nMaximum element is : {find_max(mylist)}", end=" ")