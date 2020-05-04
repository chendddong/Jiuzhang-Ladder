'''
Find the last position of a target number in a sorted array. Return -1 if
target does not exist.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1
'''

# TAG:[Binary Search, Template, Log(n)]

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            return end

        if nums[start] == target:
            return start

        return -1
# Takeaways:
# mid = (start + end) // 2
#     remember to use the parentheses
# Remember that different questions we should you different start, mid, end