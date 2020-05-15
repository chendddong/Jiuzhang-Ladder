'''
Given n pieces of wood with length L[i] (integer array). Cut them into small
pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

You couldn't cut wood into float length.
If you couldn't get >= k pieces, return 0.

Example
Example 1

Input:
L = [232, 124, 456]
k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
Example 2

Input:
L = [1, 2, 3]
k = 7
Output: 0
Explanation: It is obvious we can't make it.

Challenge
O(n log Len), where Len is the longest length of the wood.
'''

# TAG:[Binary Search, Search the answer]

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if not L:
            return 0
        
        start, end = 1, max(L)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.cut_woods(L, mid) < k:
                end = mid
            else:
                start = mid

        if self.cut_woods(L, end) >= k:
            return end
        if self.cut_woods(L, start) >= k:
            return start

        return 0

    def cut_woods(self, woods, piece):
        num_of_woods = 0
        for wood in woods:
            num_of_woods += wood // piece

        return num_of_woods

# Takeaways:
# Take proper 'Guess' of the answer you wanna search for
# decouple the functions

