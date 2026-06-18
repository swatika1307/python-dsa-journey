# Problem 1 -
with open("problem_01.txt", "r") as f:
    text = f.read()
    if "twinkle" in text:
        print("Present")
    else:
        print("Not present")

# Problem 2 -
import random

def game():
    print("You are playing the game")
    score = random.randint(1, 10)
    with open("problem_02.txt", "r") as f:
        high_score = f.read()
        if(high_score != ""):
            high_score = int(high_score)
        else:
            high_score = 0
    print(f"Your score: {score}")
    if score > high_score:
        with open("problem_02.txt", "w") as f:
            f.write(str(score))

game()

# Problem 3 -
def generateMultiplicationTable(num):
    table = ""
    for i in range(1, 11):
        table += f"{num} X {i} = {num * i}\n"
    with open(f"Tables/table_{num}.txt", "w") as f:
        f.write(table)

for num in range(2, 21):
    generateMultiplicationTable(num)

# Problem 4 -
word = "Donkey"
with open("problem_04.txt", "r") as f:
    content = f.read()
contentNew = content.replace(word, "######")
with open("problem_04.txt", "w") as f:
    f.write(contentNew)

# Problem 5 -
words = ["Donkey", "bad"]
with open("problem_05.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))
with open("problem_05.txt", "w") as f:
    f.write(content)

# Problem 6 -
with open("problem_06.html", "r") as f:
    content = f.read()
if "python" in content:
    print("Yes")
else:
    print("No")

# Problem 7 -
with open("problem_06.html", "r") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if "python" in line:
        print(f"Python present. Line no : {lineno}")
        break
    lineno += 1
else:
    print("Python not present.")

# Problem 8 -
with open("problem_08.txt", "r") as f:
    content = f.read()
with open("problem_solution_08.txt", "w") as f:
    f.write(content)

# Problem 9 -
with open("problem_08.txt", "r") as f:
    content1 = f.read()
with open("problem_solution_08.txt", "r") as f:
    content2 = f.read()
if content1 == content2:
    print("Identical files.")
else:
    print("Not identical files.")

# Problem 10 -
with open("problem_10.txt", "w") as f:
    f.write("")

# Problem 11 -
with open("problem_11.txt", "r") as f:
    content = f.read()
with open("problem_solution_11.txt", "w") as f:
    f.write(content)