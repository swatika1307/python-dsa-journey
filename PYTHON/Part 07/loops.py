# while loop - condition checked first, evaluates to true then body executes, stops execution when condition fails
i = 1
while(i <= 50):
    print(i)
    i = i + 1

l = ["Apple", "Banana", "Grapes", "Orange", "Watermelon", "Pineapple"]
i = 0
while(i < len(l)):
    print(l[i])
    i = i + 1

# for loop with range
for i in range(1, 10, 2):
    print(i)

# for loop with else
l = [1, 2, 3]
for i in l:
    print(i)
else:
    print("done")

# break
for i in range(101):
    print(i)
    if (i == 3):
        break

# continue
for i in range(4):
    if i == 2:
        continue
    print("printing ", i)

# pass
for i in range(890):
    pass # we want to write the logic later on
i = 2
while i <= 4:
    print(i) 