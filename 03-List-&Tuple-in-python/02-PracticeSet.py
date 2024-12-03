# 1)Write a program to ask ther user to enter names of their 3 favorite moves & store them in a list.
'''
listname=[]
for i in range(1,4):
    name = input(f"Enter your favorite movi name {i}: ")
    listname.append(name)
print(listname)
'''

# 2)Write a program to check if a list contains a palindrome of elements. (Hint: use copy() method()) 

'''
mylist = ['r', 'a', 'c', 'c', 'a', 'r']
listcopy = mylist.copy()
revlist = listcopy[::-1]

if(revlist == listcopy) :
    print("The list is palindrome")
else : 
    print("The list is not palindrome")
'''

# 3) Write a program to count the number of students with the "A" grade in the following tuple. 

mytuple = ("C", 'D', "A", "A", "B", "B", "A")
# print(mytuple.count("A"))

# Convert the tuple to a list
mylist = list(mytuple)
# # Store th above values in a list & sort them from "A" to "D"
mylist.sort()
print(mylist)

