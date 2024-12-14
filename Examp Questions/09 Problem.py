# Write a program to accept the string and print the number of upper-and lower-case letters.


mystring = "Kirandevi Saraf Institute Of Complete Learning"
uppercase_count = 0
lowercase_count = 0
uppercase = []
lowercase = []
for char in mystring:
    if char.isupper():
        uppercase_count += 1
        uppercase.append(char)
    elif char.islower():
        lowercase_count += 1
        lowercase.append(char)


print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")

print(f"Uppercase letter: {uppercase}")
print(f"Lowercase letter: {lowercase}")