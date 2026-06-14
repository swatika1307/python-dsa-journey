name = "Swatika"

nameLen = len(name)
print(nameLen)

nameShort = name[0:3] # start with 0, but excluding 3 - 0, 1, 2 --> Swa
print(nameShort)

char1 = name[1]
print(char1)

print(name[-5:-3])
print(name[2:4])

print(name[-4:-5]) 
print(name[3:2])

print(name[-4:-1]) 
print(name[3:6])

print(name[:3]) # default starting index is 0
print(name[0:3])

print(name[1:]) # default ending index is length
print(name[1:7])

print(name[1:5:2]) # every second character starting from 1, but before 5 gets printed