class Solution:
    # Brute force
    def intersection_of_sorted_arrays1(self, array1, array2, n, m):
        intersectionArr = []
        visited = [0] * m
        for i in range(n):
            for j in range(m):
                if(array1[i] == array2[j] and visited[j] == 0):
                    intersectionArr.append(array1[i])
                    visited[j] = 1
                    break
                if(array2[j] > array1[i]):
                    break
        return intersectionArr
    
    # Optimal
    def intersection_of_sorted_arrays2(self, array1, array2, n, m):
        intersectionArr = []
        i = 0
        j = 0
        while(i < n and j < m):
            if(array1[i] < array2[j]):
                i = i + 1
            elif(array2[j] < array1[i]):
                j = j + 1
            else:
                intersectionArr.append(array1[i])
                i = i + 1
                j = j + 1
        return intersectionArr
    
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
result = object.intersection_of_sorted_arrays2(array1, array2, n, m)

for i in range(len(result)):
    print(result[i], end = ' ')