'''
Suppose a sorted array in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
You can assume no duplicate exists in the array.

Example
Example 1:

Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
The minimum value in an array is 0.
Example 2:

Input：[2,1]
Output：1
Explanation：
The minimum value in an array is 1.
'''
# TAG:[Binary Search, Data Materialize]

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        return min(nums[start], nums[end])

# Takeaways:
# One must compare the number with the mid index with the last number to make
# sure one will be finding the 'sudden drop'