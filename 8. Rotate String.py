'''
Given a string(Given in the way of char array) and an offset, rotate the
string by offset in place. (rotate from left to right).
offset >= 0
the length of str >= 0
Make changes on the original input data

Clarification
in place means you should change string s in the function. You don't return anything.
Example
Example 1:

Input: str="abcdefg", offset = 3
Output: str = "efgabcd" 
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".
Example 2:

Input: str="abcdefg", offset = 0
Output: str = "abcdefg" 
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "abcdefg".
Example 3:

Input: str="abcdefg", offset = 1
Output: str = "gabcdef" 
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "gabcdef".
Example 4:

Input: str="abcdefg", offset =2
Output: str = "fgabcde" 
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "fgabcde".
Example 5:

Input: str="abcdefg", offset = 10
Output: str = "efgabcd" 
Explanation: Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".
Challenge
Rotate in-place with O(1) extra memory.
'''
# TAG:[Rotated using 3 steps, two pointers]

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        if not s:
            return s
        
        n = len(s)
        offset = offset % n
        self.reverse_arr(s, 0, n - offset - 1)
        self.reverse_arr(s, n - offset, n - 1)
        self.reverse_arr(s, 0, n - 1)

    def reverse_arr(self, s, start, end):
        while start < end:
            temp_val = s[end]
            s[end] = s[start]
            s[start] = temp_val
            start += 1
            end -= 1

# Takeaways:
# How to do in-place rotating. Two pointers going toward each other


























# Takeaways: