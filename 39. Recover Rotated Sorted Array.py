'''
Given a rotated sorted array, recover it to sorted array in-place.（Ascending）

Clarification
What is rotated array?

For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
Example
Example1:
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
Example2:
[6,8,9,1,2] -> [1,2,6,8,9]
Challenge
In-place, O(1) extra space and O(n) time.
'''

# TAG:[Rotated sorted array]

# Solution 1 Basic two pointer to swap elements IN PLACE
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        if not nums:
            return nums
        
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == min(nums):
                offset = i
        self.reverse_arr(nums, 0, offset - 1)
        self.reverse_arr(nums, offset, n - 1)
        self.reverse_arr(nums, 0, n - 1)

    def reverse_arr(self, nums, start, end):
        while start < end:
            temp_val = nums[end]
            nums[end] = nums[start]
            nums[start] = temp_val
            start += 1
            end -= 1

# Solution 2 Binary Search, Swap two elements in an array
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        if not nums:
            return nums

        n = len(nums)
        # Modified Binary Search
        offset = self.find_smallest_num(nums)
        self.reverse_arr(nums, 0, offset - 1)
        self.reverse_arr(nums, offset, n - 1)
        self.reverse_arr(nums, 0, n - 1)

    def reverse_arr(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def find_smallest_num(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
            else: # duplicate elements. Worst is O(n)
                end = end - 1
        
        if nums[start] < nums[end]:
            return start
        return end

# Solution 3 Add first element to the end and delete the first 
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        while nums[0] >= nums[-1]:
            nums.append(nums[0])
            del nums[0]

# Takeaways: In-Place elements swaps 