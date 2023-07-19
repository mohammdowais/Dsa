# brute force method that i could think of
def setZeroes(matrix):
    """
    https://leetcode.com/problems/set-matrix-zeroes/
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    _____________________________________________
    [        0,1,2,3
        0 | [0,1,2,0],  l[l[0]]
        1 | [3,4,5,2],  l[l[1]]
        2 | [1,3,1,5]   l[l[2]]
    ]
    """
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row:
                matrix[i][j] = 0
            if j in col:
                matrix[i][j] = 0
    for row in matrix:
        print(row)

setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])