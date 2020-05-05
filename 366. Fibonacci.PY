'''
Find the Nth number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

The first two numbers are 0 and 1.
The i th number is the sum of i-1 th number and i-2 th number.
The first ten numbers in Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
The Nth fibonacci number won't exceed the max value of signed 32-bit integer in the test cases.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:
    Input:  1
    Output: 0
    
    Explanation: 
    return the first number in  Fibonacci sequence .

Example 2:
    Input:  2
    Output: 1
    
    Explanation: 
    return the second number in  Fibonacci sequence .
'''

# TAG:[Math, No Recursion]
# 
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):  
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b

        return a
# Takeaways:
# Use variable to store the path and middle results
