# Write a python program to count odd numbers and even number in tuple.


def count_odd_even_no(mytuple):
    odd_no = 0
    even_no = 0

    for i in mytuple:
        if (i % 2 == 0):
            even_no += 1
        else: 
            odd_no += 1
    
    return odd_no, even_no

mytuple = (1,2,3,4,5,6,7,8,9,10,11,13,15)
odd_no , even_no= count_odd_even_no(mytuple)
print(f"Odd number appears {odd_no} times in tuple")
print(f"Even number appears {even_no} times in tuple")
