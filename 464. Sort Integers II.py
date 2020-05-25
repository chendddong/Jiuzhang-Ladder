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

# TAG:[QuickSort, Sort, MergeSort]

# Solution 1. QuickSort
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

# Solution 2 MergeSort
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        if not A:
            return

        temp = [None] * len(A)
        self.merge_sort(A, 0, len(A) - 1, temp)

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return

        self.merge_sort(A, start, (start + end) // 2, temp)
        self.merge_sort(A, (start + end) // 2 + 1, end, temp)
        self.merge(A, start, end, temp)

    def merge(self, A, start, end, temp):
        mid = (start + end) // 2
        # two pointers
        i, j = start, mid + 1
        # start from the 'start', not 0
        index = start

        while i <= mid and j <= end:
            if A[i] < A[j]:
                temp[index] = A[i]
                i += 1
            else:
                temp[index] = A[j]
                j += 1
            
            index += 1

        # Process the remaining numbers in the array
        while i <= mid:
            temp[index] = A[i]
            index += 1
            i += 1
        while j <= end:
            temp[index] = A[j]
            index += 1
            j += 1

        # copy values
        for index in range(start, end + 1):
            A[index] = temp[index]

# Takeaways:
# QuickSort:
#   *   two pointers
#   *   pivot number
#   *   move two pointers from border to the center
#   *   recursive
#   *   exit
# MergeSort:
#   *   divide/recursive
#   *   two pointers at start and mid + 1 and one index for the entire array
#   *   move pointers to the right, compare and record values in temp
#   *   Process the remaining numbers
#   *   Copy from temp to A