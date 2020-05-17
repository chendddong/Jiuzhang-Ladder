'''
Given an array with positive and negative numbers, find the maximum average
subarray which length should be greater or equal to given length k.
It's guaranteed that the size of the array is greater or equal to k.

Example
Example 1:

Input:
[1,12,-5,-6,50,3]
3
Output:
15.667
Explanation:
 (-6 + 50 + 3) / 3 = 15.667
Example 2:

Input:
[5]
1
Output:
5.000
'''
# TAG:[Binary Search, Search the answer, PreSum, minPresum, Array]

# Solution 1
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        start, end = min(nums), max(nums)
        delta = 0.00000001

        while end - start >= delta:
            mid = (start + end) / 2 # Do not need integer
            if self.can_find_subarray(mid, nums, k):
                start = mid
            else:
                end = mid

        return start

    def can_find_subarray(self, avg, nums, k):
        n = len(nums)
        # How to get PreSum of a given array
        presum =  [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            # Regulated PreSum, for easily calculating the answer
            presum[i] = presum[i - 1] + nums[i - 1] - avg

        # minPresum[i] -> min(presum[0:i])
        minPresum = [sys.maxsize for _ in range(n + 1)]
        for i in range(n + 1):
            minPresum[i] = min(minPresum[i - 1], presum[i])

        for i in range(k, n + 1):
            if presum[i] - minPresum[i - k] >= 0:
                return True

        return False

# Takeaways:
# Understand Presum and the application. Review this after the Presum

# Solution 2 More concise version
class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        if not nums:
            return 0
            
        start, end = min(nums), max(nums)
        while end - start > 1e-5:
            mid = (start + end) / 2
            if self.check_subarray(nums, k, mid):
                start = mid
            else:
                end = mid
                
        return start
        
    def check_subarray(self, nums, k, average):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)
            
        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])
            
        return False