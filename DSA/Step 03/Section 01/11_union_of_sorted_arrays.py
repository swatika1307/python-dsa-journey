# Union of Two Sorted Arrays
'''
Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
The union of two arrays can be defined as the common and distinct elements in the two arrays. Elements in the union should be in ascending order.
Examples:
Input:n = 5,m = 5 arr1[] = {1,2,3,4,5}  arr2[] = {2,3,4,4,5}
Output: {1,2,3,4,5}
Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1
Distnict Elemennts in arr2 are : No distinct elements.
Union of arr1 and arr2 is {1,2,3,4,5}
Input:n = 10,m = 7,arr1[] = {1,2,3,4,5,6,7,8,9,10}arr2[] = {2,3,4,4,5,11,12}
Output: {1,2,3,4,5,6,7,8,9,10,11,12}
Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1,6,7,8,9,10
Distnict Elemennts in arr2 are : 11,12
Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12}
'''

class Solution:
    # Brute force
    def union_of_sorted_arrays1(self, array1, array2, n, m):
        s = set()
        for i in range(n):
            s.add(array1[i])
        for i in range(m):
            s.add(array2[i])
        unionArr = []
        for item in s:
            unionArr.append(item)
        unionArr.sort()
        return unionArr
    
    # Optimal
    def union_of_sorted_arrays2(self, array1, array2, n, m):
        unionArr = []
        i = 0
        j = 0
        while i < n and j < m:
            if(array1[i] <= array2[j]):
                if(len(unionArr) == 0 or unionArr[-1] != array1[i]):
                    unionArr.append(array1[i])
                i = i + 1
            else:
                if(len(unionArr) == 0 or unionArr[-1] != array2[j]):
                    unionArr.append(array2[j])
                j = j + 1
        while(j < m):
            if(len(unionArr) == 0 or unionArr[-1] != array2[j]):
                unionArr.append(array2[j])
            j = j + 1
        while(i < n):
            if(len(unionArr) == 0 or unionArr[-1] != array1[i]):
                unionArr.append(array1[i])
            i = i + 1
        return unionArr

  
array1 = []
n = int(input("Enter the size of the first array: "))
for i in range(n):
    val = int(input("Enter the value: "))
    array1.append(val)

array2 = []
m = int(input("Enter the size of the second array: "))
for i in range(m):
    val = int(input("Enter the value: "))
    array2.append(val)

object = Solution()
result = object.union_of_sorted_arrays2(array1, array2, n, m)

for i in range(len(result)):
    print(result[i], end = ' ')
