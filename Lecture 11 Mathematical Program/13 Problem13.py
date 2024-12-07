# write a program to find the maximum and minimum number in the list

# def min_number(mylist):

def max_number(mylist):
    largest = mylist[0]

    for num in mylist:
        if num > largest:
            largest = num
    return largest

def min_number(mylist):
    minimum = mylist[0]

    for num in mylist:
        if num < minimum:
            minimum = num
    return minimum

mylist = [12,34,56,78,43,56,87,53,32,56,67,98]
# result = max_number(mylist)
print(f"{max_number(mylist)} is the maximum number in the list")
print(f"{min_number(mylist)} is the minimum number in the list")

