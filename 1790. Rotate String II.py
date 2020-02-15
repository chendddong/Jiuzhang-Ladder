'''
Given a string(Given in the way of char array), a right offset and a left
offset, rotate the string by offset in place.(left offest represents the offset of a string to the left,right offset represents the offset of a string to the right,the total offset is calculated from the left offset and the right offset,split two strings at the total offset and swap positions)。

Example 1:

Input：str ="abcdefg", left = 3, right = 1
Output："cdefgab"
Explanation：The left offset is 3, the right offset is 1, and the total offset is left 2. Therefore, the original string moves to the left and becomes "cdefg"+ "ab".
Example 2:

Input：str="abcdefg", left = 0, right = 0
Output："abcdefg"
Explanation：The left offset is 0, the right offset is 0, and the total offset is 0. So the string remains unchanged.
Example 3:

Input：str = "abcdefg",left = 1, right = 2
Output："gabcdef"
Explanation：The left offset is 1, the right offset is 2, and the total offset is right 1. Therefore, the original string moves to the left and becomes "g" + "abcdef".
'''

# TAG:[STRING, MOD, SLICING]
# 
# Solution 1 -- Scenario realization
class Solution:
    """
    @param str: A String
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, string, left, right):
        # corner cases
        if not string:
            return ""

        # total shift to the left
        shift = (left - right) % len(string)

        if shift >= 0:
            # moveleft
            return string[shift:] + string[:shift]
        else:
            # moveright
            return string[len(string) - 1 : len(string) - abs(shift) - 1: -1] +string[:len(string) - shift]
# Takeaways:
# negative numbers % n equals a positive number in python
# Don't use str as a variable since it's a keyword in python
# string slicing str[a:b:c] a -- [start], b -- (end), c -- steps

# Solution 2 -- Move is relative
class Solution:
    """
    @param str: A String 
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """

    def RotateString2(self, string, left, right):
        # corner cases
        if not string:
            return ""

        # total shift to left! if it is negative, it will be the same as
        # moving to left after the modulo
        shift = (left - right) % len(string)
        return string[shift:] + string[:shift]

# Takeaways:
    # abc right 2 --> cab
    # -2 % 3 = 1
    # abc left 1 --> cab
    # 1 % 3

'''
Follow-up: !!
The length of the string S is N, we have M actions, every move will be like 
move K steps either to left or right

There are restrictions regarding N,M,K, where 1 <= N,M,K<= 100,000

Example
S = "ashfahsdhfja"
N = 12
M = 5, 
K = 5, -1(left)
  = 6, 1(right)
  = 7, -1
  = 8, -1
  = 3, 1
'''





















