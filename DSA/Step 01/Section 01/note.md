## Section 01 -

- Input & Output:
1. input() takes user input as a string by default
2. Typecasting: int(input()), float(input())
3. Output using print()

- Variables & Data Types:
1. Variables store references to objects
2. Common data types - int, float, str, bool
3. Example: age = 22, name = "Swatika"

- Conditional Statements:
1. if
2. elif
3. else
4. match-case (Python 3.10+)
5. Used for decision making

- Lists (Arrays in Python):
1. Ordered and mutable
2. Common methods - append(), insert(), remove(), pop(), sort()
3. Example: nums = [1, 2, 3] nums.append(4)

- Strings:
1. Sequence of characters
2. Immutable
3. Common operations: Indexing, Slicing, Concatenation
4. Example: name = "Python" print(name[0])

- Loops:
1. For Loop: Used to iterate over sequence
for num in nums:
    print(num)
2. While Loop: Runs until condition becomes False
while x > 0:
    x -= 1
   
- Functions:
1. Reusable block of code
2. Improve readability and modularity
def greet(name):
    return f"Hello {name}"
  
- Python Memory Model:
1. Variables store references to objects
2. Mutable objects: list, dict, set
3. Immutable objects: int, float, str, tuple

- Pass-by-Object-Reference:
1. Python does not use pure pass-by-value
2. Python does not use pure pass-by-reference
3. Function parameters receive references to objects
4. Modifying an object affects the original object
5. Reassigning a variable affects only the local reference

- Time Complexity:
1. Time Complexity measures how the running time of an algorithm grows as the input size increases
2. Time Complexity is not the actual execution time
3. It measures the growth rate of an algorithm
4. We usually focus on the worst-case scenario (Big O Notation)
5. Constants are ignored
6. Lower-order terms are ignored
7. Common Complexities: O(1) - Constant Time, O(log n) - Logarithmic Time, O(n) - Linear Time, O(n²) - Quadratic Time
8. Single Loop:
for i in range(n):
    print(i)
Time Complexity: O(n)
9. Nested Loop:
for i in range(n):
    for j in range(n):
        print(i, j)
Time Complexity: O(n²)

- Space Complexity:
1. Space Complexity measures the memory used by an algorithm
2. Total Space = Input Space + Auxiliary Space
3. Auxiliary Space = Extra memory used by the algorithm apart from the input
4. Example:
arr = [1, 2, 3]
total = 0
for num in arr:
    total += num
Auxiliary Space: O(1)
