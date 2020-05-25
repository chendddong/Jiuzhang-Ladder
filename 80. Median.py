'''
Given a unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the N/2-th number after sorted.
The size of array is not exceed 10000

Example
Example 1:

Input：[4, 5, 1, 2, 3]
Output：3
Explanation:
After sorting，[1,2,3,4,5]，the middle number is 3
Example 2:

Input：[7, 9, 4, 5]
Output：5
Explanation:
After sorting，[4,5,7,9]，the second(4/2) number is 5
Challenge
O(n) time
'''

# TAG:[Quick Sort, Quick Select, Two Pointers]

# Solution #1 quick select
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        if not nums:
            return 

        # How to calculate K -- Kth largest -- median
        # if n = 5 K = 3 -> index = K - 1
        # [4, 5, 1, 2, 3] -- > Kth number is 1
        # if n = 4 K = 2 -> index = K - 1
        # [7, 9, 4, 5] -- > Kth number is 9
        
        K = (len(nums) + 1) // 2
        return self.quick_select(nums, 0, len(nums) - 1, K)

    def quick_select(self, nums, start, end, K):
        if start == end:
            return nums[start]

        # Use i, j as pointers
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
        if j >= K - 1 and start <= j:
            return self.quick_select(nums, start, j, K)
        # Go right
        if i <= K - 1 and i <= end:
            return self.quick_select(nums, i, end, K)
        # Target
        return nums[K - 1]

# Takeaways:
# Simulate the logic and relive the process!
# Always test the border index 