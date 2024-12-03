# Create a Simple List
my_list = [10,20,30,40,50]

# List functions with examples and short definations

# 1. append(x) -> Addes an element x to the ened of the list.
my_list.append(56)
print(f"Append Functions: {my_list}")  # Output: [10, 20, 30, 40, 50, 56]

# 2. extend(iterable): Adds elemets from and iterable(like another list) to the list.
my_list.extend([70,80])
print(f"Extend Functions: {my_list}")  # Output: [10, 20, 30, 40, 50, 60, 70, 80]

# 3. insert(i, x): Insertes element x at position i.
my_list.insert(2,25)
print(f"Insert Function: {my_list}") # Output: [10, 20, 25, 30, 40, 50, 60, 70, 80]

# 4. remove(x): Removes the first occurrence of element x.
my_list.remove(40)
print(f"Removed Function: {my_list}") # Output: [10, 20, 25, 30, 50, 60, 70, 80]

# 5. pop([i]): Removes and returns the element at pisition i(lat element if i is not given).
rem_item = my_list.pop(3)
print(f"Pop Function: {my_list}")  # Output: [10, 20, 25, 50, 60, 70, 80]
print(f"Remove number: {rem_item}") # Output: 30

# 6. clear(x): Removes all elements from the list.
my_list.clear()
print(f"Clear Function: {my_list}")

# 7. index(x): Returns the index of the first occurrence of element x.
my_list = [10,20,30,40,50]
print(f"Index Function: {my_list.index(30)}")

# 8. count(x): Returns the number of items element x appears in the list.
print(f"Count Function: {my_list.count(20)}") # Output: 1

# 9. sort(): Sorts the list in ascending order.
my_list.sort()
print(f"Sort Function: {my_list}") # Output: [10, 20, 30, 40, 50]

# 10. reverse(): Reverese the order of elements in the list.
my_list.reverse()
print(f"Reverse Function: {my_list}") # Output: [50, 40, 30, 20, 10]

# 11. copy(): Returns a shallow copy of the list.
new_list = my_list.copy()
print(f"Copy Function: {new_list}")  # Output: [50, 40, 30, 20, 10]
