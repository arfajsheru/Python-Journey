# 15) Write a program to display 1-50 no and display even and odd between them.

even_list = []
odd_list = []

for i in range(0,50):
    if (i % 2 == 0):
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even number list",even_list)
print("Odd number list",odd_list)