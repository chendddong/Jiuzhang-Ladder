'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example
Example 1:
    Input:  [[5]],2
    Output: false
    
    Explanation: 
    false if not included.
    
Example 2:
    Input:  [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
],3
    Output: true
    
    Explanation: 
    return true if included.
Challenge
O(log(n) + log(m)) time
'''

# TAG:[Binary Search, 2D Matrix]

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        if not matrix[0]:
            return False

        start, end = 0, len(matrix) * len(matrix[0]) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_value(matrix, mid) < target:
                start = mid
            else:
                end = mid

        return  self.get_value(matrix, start) == target or self.get_value(matrix, end) == target

    def get_value(self, matrix, index):
        x = index // len(matrix[0])
        y = index % len(matrix[0])
        return matrix[x][y]

# Takeaways: 
# Search in 2D matrix
# How to use GENERAL index to tackle down the axis in the 2D matrix:
#   * x = index // len(Matrix[0])
#   * y = index % len(Matrix[0])
# How to write the code elegantly











