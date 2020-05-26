'''
Calculate the an % b where a, b and n are all 32-bit non-negative integers.
Have you met this question in a real interview?  Yes
Problem Correction
Example
For 231 % 3 = 2

For 1001000 % 1000 = 0
Challenge
O(logn)
'''

# TAG:[Binary Search, Math, Recursion]

# Solution 1 Recursion 
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
            
        if n == 1:
            return a % b
            
        # a^n = (a^n/2) ^ 2
        power = self.fastPower(a, b, n // 2)
        power = (power * power) % b
        
        if n % 2 == 1:
            power = (power * a) % b
            
        return power

# Solution 2 Non-Recursion
class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = a * a % b
            n = n // 2
        return ans % b


# Takeaways:
# Same as 428. Pow(x, n)
