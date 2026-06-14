# Problem 1 -
name = input("Enter your name: ")
print(name + ", Good afternoon!")

# Problem 2 -
name = input("Enter your name: ")
date = input("Enter date (dd/mm/yyy): ")
letter = print(f'''Dear {name},
You are selected.
{date}''')

# Problem 3 -
s = "I am   good  girl."
print(s.find("  "))

# Problem 4 -
s = "I am   good  girl."
print(s.replace("  ", " "))

# Problem 5 -
letter = "Dear XYZ,\n\tThis python course is nice.\nThanks!"
print(letter)


# Word of caution
# Strings are immutable, which means even after performing these operations the original string stays the same.
# After operations a new string is formed.