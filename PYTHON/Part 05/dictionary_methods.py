marks = {
    'Swatika' : 100,
    'Rohan' : 23,
    'Akash' : 78
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Swatika" : 99, "Renuka" : 96})
print(marks)

print(marks.get("Rohan"))

print(marks.get("Shivika")) # None - does not give error

value = marks.pop('Rohan')
print(value)
print(marks)

result = marks.popitem()
print(result)
print(marks)