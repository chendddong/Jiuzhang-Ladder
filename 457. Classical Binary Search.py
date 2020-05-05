'''
Find any position of a target number in a sorted array. Return -1 if target does not exist.

Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 1 or 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1
'''

# Solution 1 No recursion
# TAG:[Binary Search, Template, Log(n), Recursion]

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid

        # Based on what you need exactly
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1

# Takeaways:
# not nums :
#   1.  nums is None(null)
#   2.  nums is empty([])
# Remember that different questions should be using different start, mid, end

# with if and return, the next statement should be 'if' not elif
#   see line from 39 to 42