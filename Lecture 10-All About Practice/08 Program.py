# Display Fibonacci series up to 10 terms

# num1 , num2 = 0, 1

# for i in range(10):
#     print(num1 , end=" ")
#     res = num1 + num2

#     num1 = num2
#     num2 = res




num = int(input("Please enter number: "))

num1, num2 = 0, 1
for i in range (num):
    print(num1, end=" ")

    res = num1 + num2

    num1 = num2
    num2 = res



