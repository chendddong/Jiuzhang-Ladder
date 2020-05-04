'''
For a given sorted array (ascending order) and a target number, find the
first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:
    Input:  [1,4,4,5,7,7,8,9,9,10]，1
    Output: 0
    
    Explanation: 
    the first index of  1 is 0.

Example 2:
    Input: [1, 2, 3, 3, 4, 5, 10]，3
    Output: 2
    
    Explanation: 
    the first index of 3 is 2.

Example 3:
    Input: [1, 2, 3, 3, 4, 5, 10]，6
    Output: -1
    
    Explanation: 
    Not exist 6 in array.
'''

# TAG:[Binary Search, Template, Log(n)]
# TAG:[Binary Search, Template, Log(n)]
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
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

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1