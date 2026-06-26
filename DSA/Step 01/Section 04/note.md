## Section 04 - Collections in Python

- What are Collections?
1. Collections are built-in data structures provided by Python to efficiently store and manipulate data
2. The primary collections used in DSA are: List, Tuple, Set, Dictionary, Collections Module (Counter, defaultdict, deque), Heap (heapq)

- List:
1. Definition: A list is an ordered, mutable collection that allows duplicate elements
2. Common Operations: nums.append(40), nums.insert(1, 15), nums.remove(20), nums.pop(), nums.pop(0), nums.sort(), nums.reverse(), len(nums)
3. Access (arr[i]) = O(1), Update = O(1), Append = O(1), Pop(Last) = O(1), Insert Beginning = O(n), Remove/Search = O(n), Sort = O(n log n)
4. Used When: Maintaining order, Duplicates are allowed, Frequent indexing is required

- Tuple:
1. Definition: A tuple is an ordered, immutable collection
2. Features: Cannot modify elements, Faster than lists, Can be used as dictionary keys
3. Access = O(1), Search = O(n)
4. Used When: Data should never change.

- Set:
1. Definition: A set is an unordered collection of unique elements
2. Common Operations: nums.add(5), nums.remove(2), nums.discard(10), nums.clear()
3. Add = O(1), Remove = O(1), Search = O(1), Union = O(n), Intersection = O(min(n,m))
4. Used When: Removing duplicates, Fast searching, Membership checking

- Dictionary (Hash Map):
1. Definition: Stores data in key-value pairs
2. Common Operations: marks["Alice"], marks.get("Bob"), marks.keys(), marks.values(), marks.items(), marks.pop("Bob"
3. Insert = O(1), Search = O(1), Delete = O(1), Update = O(1)
4. Used When: Frequency counting, Mapping values, Constant-time lookup

- Collections Module: from collections import Counter, defaultdict, deque

- Counter:
1. Automatically counts frequencies
2. Used When: Frequency counting problems

- defaultdict: Provides a default value for missing keys

- deque:
1. Double-ended queue
2. Append = O(1), Append Left = O(1), Pop = O(1), Pop Left = O(1)
3. Used in: BFS, Sliding Window, Queue implementation

- Heap:
1. Used for: Priority Queue, Top K Problems, Heap Data Structure
