'''
Given target, a non-negative integer k and an integer array A sorted in
ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.
The value k is a non-negative integer and will always be smaller than the 


Example
Example 1:

Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
Example 2:

Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
Challenge
O(logn + k) time
'''

# TAG:[Binary Search, Two pointers, Decouple, Materialize]

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        right = self.findUpperClosest(A, target)
        left = right - 1

        result = []
        # moving two indices from adjacent to far away
        for _ in range(k):
            if self.isLeftCloser(A, target, left, right):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1

        return result

    def findUpperClosest(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target: # first position
                end = mid
            else:
                start = mid

        if A[start] >= target:
            return start

        if A[end] >= target:
            return end

        # all numbers are smaller than the target
        return len(A)

    def isLeftCloser(self, A, target, left, right):
        # No left numbers left
        if left < 0:
            return False
        # index is at the right most
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target

# Takeaways:
# How to handle the Kth problem
# NEAREST means there could be possibilities that answers are on both sides
# COMPARISON target - A[left] <= A[right] - target
# Two Pointers and Binary Search Template


