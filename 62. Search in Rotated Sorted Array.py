'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input: [4, 5, 1, 2, 3] and target=1, 
Output: 2.
Example 2:

Input: [4, 5, 1, 2, 3] and target=0, 
Output: -1.
Challenge
O(logN) time
'''

# TAG:[Binary Search, Data Materialize]

# Solution 1 Binary search with condition

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= A[start]: # M'
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else: # M"
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1

# Takeaways:
# Take chances on the conditions

# Solution 2 Find the minimum, use binary search twice

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1

        index = self.find_min(A)
        if A[index] <= target <= A[-1]:
            return self.binary_search(A, index, len(A) - 1, target)
        return self.binary_search(A, 0, index - 1, target)


    def find_min(self, A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[end]:
                start = mid
            else:
                end = mid

        # Need index not the value
        if A[start] < A[end]:
            return start
        return end

    def binary_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1