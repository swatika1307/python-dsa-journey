# Problem 1 -
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
if (num1 > num2 and num1 > num3 and num1 > num4):
    print(f"{num1} is greatest")
elif (num2 > num1 and num2 > num3 and num2 > num4):
    print(f"{num2} is greatest")
elif (num3 > num1 and num3 > num2 and num3 > num4):
    print(f"{num3} is greatest")
else:
    print(f"{num4} is greatest")

# Problem 2 -
marks1 = int(input("Enter the first subject marks: "))
marks2 = int(input("Enter the second subject marks: "))
marks3 = int(input("Enter the third subject marks: "))
total_percentage = (marks1 + marks2 + marks3)/3
if(marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and total_percentage >= 40):
    print("Woohhoo, you passed!")
else:
    print("You failed, try again!")

# Problem 3 -
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
comment = input("Enter your comment: ")
if ((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("Spam comment")
else:
    print("Not spam comment")

# Problem 4 -
username = input("Enter username: ")
if len(username) < 10:
    print("Username length is less that 10.")
else:
    print("Username length is greater than or equal to 10.")

# Problem 5 -
l = ['Rohan', 'Divya', 'Swatika', 'Akshay']
num = input("Enter the number: ")
if num in l:
    print("Present")
else:
    print("Absent")

# Problem 6 -
marks = int(input("Enter the marks: "))
if (marks >= 90):
    print("Grade: Ex")
elif (marks >= 80):
    print("Grade: A")
elif (marks >= 70):
    print("Grade: B")
elif (marks >= 60):
    print("Grade: C")
elif (marks >= 50):
    print("Grade: D")
else:
    print("Grade: F")

# Problem 7 -
post = input("Enter the post: ")
if 'Swatika'.lower() in post.lower():
    print("Post speaks about Swatika")
else:
    print("Post does not speak about Swatika")