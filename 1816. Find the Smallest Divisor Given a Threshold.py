'''
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.
1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4
'''

# TAG:[Binary Search, Search the answer]

class Solution:
    """
    @param nums: an array of integers
    @param threshold: an integer
    @return: return the smallest divisor
    """
    def smallestDivisor(self, nums, threshold):
        if not nums:
            return -1

        start, end = 1, max(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_smaller_than_threshold(mid, nums, threshold):
                end = mid
            else:
                start = mid

        if self.is_smaller_than_threshold(start, nums, threshold):
            return start
        return end

    def is_smaller_than_threshold(self, divisor, nums, threshold):
        sum_divide = 0
        for num in nums:
            # math.ceil(num / divisor)
            sum_divide += (num + divisor - 1) // divisor

        return sum_divide <= threshold

# Takeaways:
# Take proper 'Guess' of the answer you wanna search for