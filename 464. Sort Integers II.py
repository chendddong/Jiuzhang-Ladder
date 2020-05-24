'''Given an integer array, sort it in ascending order in place. Use quick sort,
merge sort, heap sort or any O(nlogn) algorithm.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example1:

Input: [3, 2, 1, 4, 5], 
Output: [1, 2, 3, 4, 5].
Example2:

Input: [2, 3, 1], 
Output: [1, 2, 3].
'''

# TAG:[QuickSort, Sort]

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        if not A:
            return

        self.quick_sort(A, 0, len(A) - 1)

    def quick_sort(self, A, start, end):
        # exit
        if start >= end:
            return

        i, j = start, end
        # a number
        pivot = A[(i + j) // 2]

        while i <= j:
            while i <= j and A[i] < pivot:
                i += 1
            while i <= j and A[j] > pivot:
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

        self.quick_sort(A, start, j)
        self.quick_sort(A, i, end)

# Takeaways:
# 1.    exit
# 2.    pivot is a number
# 3.    when comparing, index is with '=', pivot without '='