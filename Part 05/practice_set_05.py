# Problem 1 -
words = {
    'madad' : 'help',
    'kursi' : 'chair',
    'tum' : 'you'
}
word = input("Enter the word: ")
print(words[word])

# Problem 2 - 
s = set()
value = int(input("Enter the value: "))
s.add(value)
value = int(input("Enter the value: "))
s.add(value)
value = int(input("Enter the value: "))
s.add(value)
value = int(input("Enter the value: "))
s.add(value)
value = int(input("Enter the value: "))
s.add(value)
value = int(input("Enter the value: "))
s.add(value)
value = int(input("Enter the value: "))
s.add(value)
value = int(input("Enter the value: "))
s.add(value)
print(s)


# Problem 3 - 
a = {18, '18'}
print(a)

# Problem 4 -
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

# Problem 5 -
s = {}
print(type(s))

# Problem 6 -
d = {}
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
print(d)

# Problem 7 - the value gets updated
d = {}
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
print(d)

# Problem 8 - no problem
d = {}
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
name = input("Enter name: ")
lang = input("Enter language: ")
d.update({name : lang})
print(d)

# Problem 9 -
s = {8, 7, 12, "Harry", [1,2]}
s[4][0] = 4 # not happening - list cannot be loaded in a set, you cannot index a set