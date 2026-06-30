## Section 02 - Sorting II

- Problems:
1. Merge sort
2. Quick sort
3. Recursive bubble sort
4. Recursive insertion sort

- Patterns Learned:
1. Selection Pattern: Find the minimum (or maximum) element from the unsorted portion and place it at its correct position
2. Adjacent Swapping: Repeatedly compare and swap adjacent elements until the largest (or smallest) element reaches its correct position
3. Insertion Pattern: Maintain a sorted left portion and insert the current element into its correct position
4. Divide & Conquer: Break the array into smaller subarrays, solve them recursively, and combine the results
5. Merge Technique: Merge two already sorted arrays into a single sorted array using two pointers
6. Pivot Partitioning: Choose a pivot element and partition the array such that elements smaller than the pivot are on the left and larger elements are on the right (Quick Sort)
7. Recursive Implementation: Convert iterative algorithms into recursive ones without changing the underlying logic
8. In-place vs Extra Space:
   - In-place: Selection, Bubble, Insertion, Quick Sort
   - Extra Space: Merge Sort
9. Stability:
   - Stable: Bubble, Insertion, Merge
   - Unstable: Selection, Quick
10. Complexity Awareness:
    - O(n²): Selection, Bubble, Insertion
    - O(n log n): Merge, Quick (Average Case)
    - O(n²): Quick Sort (Worst Case)
