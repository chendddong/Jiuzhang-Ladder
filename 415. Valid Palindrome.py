'''
Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Example
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"

Example 2:

Input: "race a car"
Output: false
Explanation: "raceacar"

Challenge
O(n) time without extra memory.
'''

# TAG:[STRING, TWO POINTERS, CLEAN-STRING]


# Solution 1 O(n) Take care of the string beforehand
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # corner cases
        # Null
        if s == None:
            return False
        # ""
        if not s:
            return True

        # clean up the string only num and char allowed
        new_s = ''.join(e for e in s if e.isalnum()).lower()

        # determine if the string is a valid palindrome
        return self.is_palindrome(new_s)
    
    def is_palindrome(self, s):
        start, end = 0, len(s) - 1 
        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1
        return True
# Takeaways:
# How to clean up a string
# Simulate the process and do use examples to test the cases
# / results in float and // results in int

# Solution 2 Direct compare, handle later
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:

            # control the quality of the char and determine that later
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            # see if it's palindrome one char by char
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end   -= 1

        return True



