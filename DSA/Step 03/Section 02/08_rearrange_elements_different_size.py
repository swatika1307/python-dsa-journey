class Solution:
    def rearrange_elements_different_size(self, array, size):
        pos = []
        neg = []
        for i in range(size):
            if(array[i] > 0):
                pos.append(array[i])
            else:
                neg.append(array[i])
        if(len(pos) > len(neg)):
            for i in range(len(neg)):
                array[2 * i] = pos[i]
                array[2 * i + 1] = neg[i]
            idx = 2 * len(neg)
            for i in range(len(neg), len(pos)):
                array[idx] = pos[i]
                idx = idx + 1
        else:
            for i in range(len(pos)):
                array[2 * i] = pos[i]
                array[2 * i + 1] = neg[i]
            idx = 2 * len(pos)
            for i in range(len(pos), len(neg)):
                array[idx] = neg[i]
                idx = idx + 1
        return array
    
array = []
size = int(input("Enter the size: "))
for i in range(size):
    val = int(input("Enter the value: "))
    array.append(val)

object = Solution()
result = object.rearrange_elements_different_size(array, size)

for i in range(len(result)):
    print(result[i], end = ' ')