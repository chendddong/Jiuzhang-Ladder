'''Given a string s, find the longest palindromic subsequence's length in s.

You may assume that the maximum length of s is 1000.

Example
Example1

Input: "bbbab"
Output: 4
Explanation:
One possible longest palindromic subsequence is "bbbb".
Example2

Input: "bbbbb"
Output: 5
'''
# TAG:[DP]

# Solution 1 O(n^2)
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # Write your code here
        length = len(s)
        if length == 0:
            return 0

        dp = [[0 for _ in range(length)] for __ in range(length)]
        
        for i in range(length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][length - 1]

# Takeaways: DP later[01202020]
