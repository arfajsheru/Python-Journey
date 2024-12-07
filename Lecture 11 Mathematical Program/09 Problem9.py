# 9)Write a Python function gretest_num that finds and prints the largest number from the list [12, 45, 76, 78, 94, 23, 43, 56, 78] without using built-in functions like max().

def gretest_num():
    mylist = []
    listsize = int(input("Enter your number list length: "))
    for i in range(1, listsize):
        num = int(input(f"Enter your number {i}: "))
        mylist.append(num)

    largest = mylist[0]
    for num in mylist:
        if num > largest:
            largest = num
    print(f"The largest number is: {largest}")
gretest_num()