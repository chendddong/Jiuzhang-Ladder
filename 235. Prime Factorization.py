'''
Prime factorize a given integer.
You should sort the factors in ascending order.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input: 10
Output: [2, 5]
Example 2:

Input: 660
Output: [2, 2, 3, 5, 11]
'''
# TAG:[Math, O(sqrt N)]
# 

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        result = []
        up = int(math.sqrt(num))

        k = 2
        while k <= up and num > 1:
            while num % k == 0:
                num //= k
                result.append(k)
            k += 1chuc

        if num > 1:
            result.append(num)

        return result

# Takeaways:
# Smartly select algorithm to reduce the process time