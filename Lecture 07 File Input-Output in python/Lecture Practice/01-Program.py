# Solution 1: Using raw string
# f = open(r"C:\Users\Arfaj sheru\OneDrive\Desktop\Python-journey\Lecture 07 File Input-Output in python\Lecture Practice\demo.txt", "a+")
# f.write("Then I'll move to React js\n")
# line = f.read()
# print(line)

# line1 = f.readline()
# print(line1)


import os
with open(r"C:\Users\Arfaj sheru\OneDrive\Desktop\Python-journey\Lecture 07 File Input-Output in python\Lecture Practice\demo.txt", "r+") as f:
    # f.write("Hii Arfaj\n")
    data = f.read()
    print(data)
    os.remove(r"C:\Users\Arfaj sheru\OneDrive\Desktop\Python-journey\Lecture 07 File Input-Output in python\Lecture Practice\sample.txt")