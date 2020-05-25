'''
Find the kth smallest number in an unsorted integer array.

Example
Example 1:

Input: [3, 4, 1, 2, 5], k = 3
Output: 3

Example 2:

Input: [1, 1, 1], k = 2
Output: 1

Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.
'''
# TAG:[Quick Sort, Quick Select, Two Pointers]

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        return self.quick_select(nums, 0, len(nums) - 1, k)

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