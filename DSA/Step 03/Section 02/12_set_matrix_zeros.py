# Set Matrix Zero
'''
Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix..
Examples:
Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0.
'''

class Solution:
    # Brute
    def mark_row(self, i, array, col):
        for j in range(col):
            if(array[i][j] != 0):
                array[i][j] = -1

    def mark_col(self, j, array, row):
        for i in range(row):
            if(array[i][j] != 0):
                array[i][j] = -1

    def set_matrix_zeros1(self, array, row, col):
        for i in range(row):
            for j in range(col):
                if(array[i][j] == 0):
                    self.mark_row(i, array, col)
                    self.mark_col(j, array, row)
        for i in range(row):
            for j in range(col):
                if(array[i][j] == -1):
                    array[i][j] = 0
        return array
    
    # Better
    def set_matrix_zeros2(self, array, row, col):
        rowMat = [0] * row
        colMat = [0] * col
        for i in range(row):
            for j in range(col):
                if(array[i][j] == 0):
                    rowMat[i] = 1
                    colMat[j] = 1
        for i in range(row):
            for j in range(col):
                if(rowMat[i] or colMat[j]):
                    array[i][j] = 0
        return array
    
    # Optimal
    def set_matrix_zeros3(self, array, row, col):
        col0 = 1
        for i in range(row):
            for j in range(col):
                if(array[i][j] == 0):
                    array[i][0] = 0
                    if(j != 0):
                        array[0][j] = 0
                    else:
                        col0 = 0
        for i in range(1, row):
            for j in range(1, col):
                if(array[i][j] != 0):
                    if(array[i][0] == 0 or array[0][j] == 0):
                        array[i][j] = 0
        if(array[0][0] == 0):
            for j in range(col):
                array[0][j] = 0
        if col0 == 0:
            for i in range(row):
                array[i][0] = 0
        return array
    
array = []
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
for i in range(row):
    current_row = []
    for j in range(col):
        print(f"Enter the value of array[{i}][{j}]:", end = ' ')
        val = int(input())
        current_row.append(val)
    array.append(current_row)

object = Solution()
result = object.set_matrix_zeros3(array, row, col)

for i in range(row):
    for j in range(col):
        print(result[i][j], end = ' ')
    print()