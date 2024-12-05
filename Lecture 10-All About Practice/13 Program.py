# Print the following pattern

#        * 
#        * * 
#        * * * 
#        * * * * 
#        * * * * * 
#        * * * * 
#        * * * 
#        * * 
#        *


num = int(input("Please enter number: "))

for i in range(1 , num + 1):
    print("* " * i)

for j in range(num - 1, 0 , -1):
    print("* " * j)
