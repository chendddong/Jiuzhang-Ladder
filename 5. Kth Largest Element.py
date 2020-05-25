'''
Find K-th largest element in an array.
You can swap elements in the array

Example
Example 1:

Input:
n = 1, nums = [1,3,4,2]
Output:
4
Example 2:

Input:
n = 3, nums = [9,3,2,4,8]
Output:
4
Challenge
O(n) time, O(1) extra memory.
'''

# TAG:[Quick Sort, Quick Select, Two Pointers]

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # test the border for 'k' using those examples
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - n + 1)

    def quick_select(self, nums, start, end, k):
        if start >= end:
            return nums[start]

        i, j = start, end
        pivot = nums[(i + j) // 2]

        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # Go left
        if j >= k - 1 and start <= j:
            return self.quick_select(nums, start, j, k)
        # Go right
        if i <= k - 1 and i <= end:
            return self.quick_select(nums, i, end, k)
        # Target
        return nums[k - 1]

# Takeaways: