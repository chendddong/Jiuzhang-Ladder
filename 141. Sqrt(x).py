'''
Implement int sqrt(int x).

Compute and return the square root of x.

Example
Example 1:
    Input:  0
    Output: 0


Example 2:
    Input:  3
    Output: 1
    
    Explanation:
    return the largest integer y that y*y <= x. 
    
Example 3:
    Input:  4
    Output: 2
'''

# TAG:[Binary Search, Thinking about the situation]

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x == 0:
            return 0

        start, end = 1, x

        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid <= x:
                start = mid
            else:
                end = mid

        if end * end <= x:
            return end
        return start

# Takeaways:
# Binary Search the answer
