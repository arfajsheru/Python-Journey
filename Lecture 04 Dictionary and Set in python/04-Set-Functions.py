# Create a simple set
my_set = {1, 2, 3, 4}

# 1. add(): Adds an element to the set.
my_set.add(5)
print(f"Add Function: {my_set}")  # Output: {1, 2, 3, 4, 5}

# 2. clear(): Removes all elements from the set.
my_set.clear()
print(f"Clear Function: {my_set}")  # Output: set()

# Resetting the set for further examples
my_set = {1, 2, 3, 4}

# 3. copy(): Returns a shallow copy of the set.
new_set = my_set.copy()
print(f"Copy Function: {new_set}")  # Output: {1, 2, 3, 4}

# 4. difference(): Returns the difference of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Difference Function: {set1.difference(set2)}")  # Output: {1, 2}

# 5. difference_update(): Removes elements found in another set.
set1.difference_update(set2)
print(f"Difference Update Function: {set1}")  # Output: {1, 2}

# 6. discard(): Removes an element without raising an error if not found.
my_set.discard(2)
print(f"Discard Function: {my_set}")  # Output: {1, 3, 4}

# 7. intersection(): Returns the intersection of two sets.
set3 = {2, 3, 4}
print(f"Intersection Function: {my_set.intersection(set3)}")  # Output: {3, 4}

# 8. intersection_update(): Updates the set with the intersection.
my_set.intersection_update(set3)
print(f"Intersection Update Function: {my_set}")  # Output: {3, 4}

# 9. isdisjoint(): Checks if two sets have no elements in common.
print(f"Isdisjoint Function: {my_set.isdisjoint({5, 6})}")  # Output: True

# 10. issubset(): Checks if a set is a subset of another set.
print(f"Issubset Function: {my_set.issubset({3, 4, 5})}")  # Output: True

# 11. issuperset(): Checks if a set is a superset of another set.
print(f"Issuperset Function: {my_set.issuperset({3})}")  # Output: True

# 12. pop(): Removes and returns an arbitrary element.
element = my_set.pop()
print(f"Pop Function: {element}, Set after pop: {my_set}")  # Output: 3, Set after pop: {4}

# Resetting the set for more examples
my_set = {1, 2, 3, 4}

# 13. remove(): Removes the specified element.
my_set.remove(1)
print(f"Remove Function: {my_set}")  # Output: {2, 3, 4}

# 14. symmetric_difference(): Returns elements in either set but not both.
print(f"Symmetric Difference Function: {my_set.symmetric_difference({3, 5})}")  # Output: {2, 4, 5}

# 15. symmetric_difference_update(): Updates the set with the symmetric difference.
my_set.symmetric_difference_update({2, 5})
print(f"Symmetric Difference Update Function: {my_set}")  # Output: {3, 4, 5}

# 16. union(): Returns the union of sets.
print(f"Union Function: {my_set.union({6, 7})}")  # Output: {3, 4, 5, 6, 7}

# 17. update(): Updates the set with the union of itself and another set.
my_set.update({6, 7})
print(f"Update Function: {my_set}")  # Output: {3, 4, 5, 6, 7}
