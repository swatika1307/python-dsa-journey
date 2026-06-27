## Section 06 - Basic Recursion

- Problems:
1. Print name N times
2. Print 1 to N
3. Print N to 1
4. Print 1 to N using backtracking
5. Print N to 1 using becktracking
6. Sum of first N natural numbers
7. Factorial of a number
8. Reverse an array
9. Check if string is palindrome
10. Finacci series

- Patterns Learned:
1. Base Case: Every recursive function must have a stopping condition
2. Smaller Subproblem: Solve the current problem by reducing it to a smaller instance (usually n-1)
3. Trust Recursion: Solve one step and let the recursive call solve the remaining problem
4. Work Before/After Call: Placing the operation before or after the recursive call changes the output
5. Parameterized vs Functional Recursion: Pass the answer as a parameter or return it from recursive calls
6. Two-Pointer Recursion: Use left and right pointers for problems like Reverse Array and Palindrome Check
7. Multiple Recursive Calls: One function can generate multiple recursive calls (e.g., Fibonacci)
8. Call Stack: Every recursive call occupies stack memory until the base case is reached
9. Complexity Awareness: Time depends on the number of recursive calls, and space depends on the recursion depth
