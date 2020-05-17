'''
You have one chocolate bar that consists of some chunks. Each chunk has its
own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.
0 <= K < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
'''

# TAG:[Binary Search, Search the answer]

class Solution:
    """
    @param sweetness: an integer array
    @param K: an integer
    @return:  return the maximum total sweetness of the piece
    """
    def maximizeSweetness(self, sweetness, K):
        if not sweetness:
            return -1

        start, end = 0, sum(sweetness)
        while start + 1 < end:
            mid = (start + end) // 2
            # more than K friends have at least mid sweetness
            if self.all_happy_with_sweets(mid, sweetness, K):
                start = mid
            else:
                end = mid

        if self.all_happy_with_sweets(start, sweetness, K):
            return end
        return start

    def all_happy_with_sweets(self, min_sweet, sweetness, K):
        temp_sweet = 0
        people = 0

        for chocolate in sweetness:
            temp_sweet += chocolate
            if temp_sweet > min_sweet:
                people += 1
                temp_sweet = 0

        return people >= K + 1

# Takeaways:
# think about the conditions and simulate the result
# Always remember to check the result with one sample before submit