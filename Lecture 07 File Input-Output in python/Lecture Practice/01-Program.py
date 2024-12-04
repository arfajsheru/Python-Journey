# Solution 1: Using raw string
f = open(r"C:\Users\Arfaj sheru\OneDrive\Desktop\Python-journey\Lecture 07 File Input-Output in python\Lecture Practice\demo.txt", "r")
data = f.read()
print(data)        # Prints content of the file
print(type(data))  # Prints type of 'data', which will be <class 'str'>
f.close()          # Always close the file after reading
