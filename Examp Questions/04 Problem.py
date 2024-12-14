# Write a python program to sum all the item in list.

def sum_list(mylist):
    sum = 0
    for i in mylist:
        sum = sum + i  
    return sum




mylist = [12,34,6,5,34,43,45]
result = sum_list(mylist)

print(f"Sum of list is: {result}")
