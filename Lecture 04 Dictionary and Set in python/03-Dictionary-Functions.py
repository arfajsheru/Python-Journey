# Create a simple dictionary 
my_dict = {'a': 1, 'b' : 2, 'c': 3}

# 1. clear(): Removes all element from the dictionary.
my_dict.clear()
print(f"Clear Function: {my_dict}") # Output: {}

# 2. copy(): Returns a shallow copy of the dictionary.
my_dict = {'a': 1, 'b' : 2, 'c': 3}
new_dict = my_dict.copy()
print(f"Copy Function: {new_dict}") # Output: {'a': 1, 'b': 2, 'c': 3}

# 3. fromkeys(): Creates a dictionay with specified keys and a single value.
new_dict = dict.fromkeys(['x','y','z'],0)
print(f"Fromkeys Function: {new_dict}")  # Output: {'x': 0, 'y': 0, 'z': 0}

# 4. get(): Returns the value of the specified key.
value = my_dict.get('b')
print(f"Get Function: {value}")

# 5. items(): Returns a list of key-value pairs as tuples.
print(f"Items Function: {my_dict.items()}")  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 6. keys(): Returns a list of all keys in the dictionay.
print(f"Keys Function: {my_dict.keys()}")  # Output: dict_keys(['a', 'b', 'c'])

# 7. pop(): Removes the specified key and returns its value.
removed_value = my_dict.pop("a")
print(f"Remove value: {removed_value}")  # Output: ('c', 3)
print(f"Pop Function: {my_dict}")        # Output: {'a': 1, 'b': 2}

# 8. popitem(): Removes and returns the last inserted key-value pair.
my_dict = {'a': 1, 'b' : 2, 'c': 3}
last_item = my_dict.popitem()
print(f"Remove last item: {last_item}")
print(f"Popitem Function: {my_dict}")


# 9. setdefault(): Returns the value of the key, and inserts it with a default value if the key doesn't exist.
my_dict = {'a': 1, 'b' : 2, 'c': 3}
value = my_dict.setdefault('d', 4)
print(f"Set Default value: {value}")     # Output: 4
print(f"Setdefault Function: {my_dict}")   # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 10. update(): Updates the dictionary with the specified key-value pairs.
my_dict.update({'e': 5, 'f': 6})
print(f"Update Function: {my_dict}")  # Output: {'a': 1, 'b': 2, 'c': 3, 'e': 5, 'f': 6}

# 11. values(): Retunrs a list of all the values in the dictionary.
print(f"Values Function: {my_dict.values()}")  # Output: dict_values([1, 2, 3])