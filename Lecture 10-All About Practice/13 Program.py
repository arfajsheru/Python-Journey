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


# num = int(input("Please enter number: "))

# for i in range(1 , num + 1):
#     print("* " * i)

# for j in range(num - 1, 0 , -1):
#     print("* " * j)

a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n1+n2+n3+n4)