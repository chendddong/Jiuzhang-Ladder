
'''
Given a string S, find the longest palindromic substring in S. You may assume
that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

'''
Example 1:

Input:"abcdzdcab"
Output:"cdzdc"

Example 2:

Input:"aba"
Output:"aba"

Challenge
O(n2) time is acceptable. Can you do it in O(n) time.
'''

# TAG:[FUNCTION, STRING, ENUMERATION]

# Solution 1 Enumeration O(n^2)
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # Corner cases None or ""
        if not s:
            return ""

        longest = ''
        # traverse the middle 
        for middle in range(len(s)):
            # odd string
            sub = self.find_longest_panlindrome(s, middle, middle)
            if len(sub) > len(longest):
                longest = sub
            # even string
            sub = self.find_longest_panlindrome(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub
        
        return longest

    def find_longest_panlindrome(self, s, left, right):
        # mind the boundaries and do a quick test.
        while (left >= 0 and right <= len(s) - 1) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]
        
# Takeaway
# When you call the function, use self.f(...)
# When you write the function, define it as f(self, ...)

# Solution 2 Interval Dynamic Programming O(n^2) NEED REVIEW
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return ""

        n = len(s)
        # create a 2 dimensional array with ease
        is_palindrome = [[False] * n for _ in range (n)]
        for i in range(n):
            # a single string itself
            is_palindrome[i][i] = True
        for i in range(1, n):
            # all the empty string we'll use them later
            is_palindrome[i][i - 1] = True

        # s = "abccba"
        # n = 6
        # is_palindrome = [
        #                 [1,0,0,0,0,0],
        #                 [1,1,0,0,0,0],
        #                 [0,1,1,0,0,0],
        #                 [0,0,1,1,0,0],
        #                 [0,0,0,1,1,0],
        #                 [0,0,0,0,1,1],
        #                 ]

        longest, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j] and length + 1 > longest:
                    longest = length + 1
                    start, end = i, j
                    
        return s[start:end + 1]

# Takeaways, use examples to go over the algorithm


# Solution 3 Manacher's Algorithm O(n) -- Optional
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return

        # Using manacher's algorithm
        # abba => #a#b#b#a#
        chars = []
        for c in s:
            chars.append('#')
            chars.append(c)
        chars.append('#')
        
        n = len(chars)
        palindrome = [0] * n
        palindrome[0] = 1
        
        mid, longest = 0, 1
        for i in range(1, n):
            length = 1
            if mid + longest > i:
                mirror = mid - (i - mid)
                length = min(palindrome[mirror], mid + longest - i)

            while i + length < len(chars) and i - length >= 0:
                if chars[i + length] != chars[i - length]:
                    break;
                length += 1
            
            if length > longest:
                longest = length
                mid = i
            
            palindrome[i] = length
        
        # remove the extra #
        longest = longest - 1
        start = (mid - 1) // 2 - (longest - 1) // 2
        return s[start:start + longest]






