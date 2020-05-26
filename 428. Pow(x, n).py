'''
Implement pow(x, n). (n is an integer.)
You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

Example
Example 1:

Input: x = 9.88023, n = 3
Output: 964.498
Example 2:

Input: x = 2.1, n = 3
Output: 9.261
Example 3:

Input: x = 1, n = 0
Output: 1
Challenge
O(logn) time
'''

# TAG:[Binary Search, Math, Recursion]

# Solution 1 Non-Recursion --> Math
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # corner case unify
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        temp = x

        while n != 0:
            if n % 2 == 1:
                ans *= temp
            temp *= temp
            n //= 2

        return ans

# Solution 2 Recursion
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n            
        return self.dfs(x, n)

    def dfs(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x        
        # a^n = (a^n/2) ^ 2
        power = self.dfs(x, n // 2)
        power *= power

        if n % 2 == 1:
            power *= x

        return power


# Takeaways:
# Must master both versions