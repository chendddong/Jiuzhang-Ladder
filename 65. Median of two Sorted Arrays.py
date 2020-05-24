'''There are two sorted arrays A and B of size m and n respectively. Find the
median of the two sorted arrays.

Clarification
The definition of the median:

The median here is equivalent to the median in the mathematical definition.

The median is the middle of the sorted array.

If there are n numbers in the array and n is an odd number, the median is A[(n-1)/2].

If there are n numbers in the array and n is even, the median is (A[n / 2] + A[n / 2 + 1]) / 2.

For example, the median of the array A=[1,2,3] is 2, and the median of the array A=[1,19] is 10.

Example
Example 1

Input:
A = [1,2,3,4,5,6]
B = [2,3,4,5]
Output: 3.5
Example 2

Input:
A = [1,2,3]
B = [4,5]
Output: 3
Challenge
The overall run time complexity should be O(log (m+n)).
'''

# TAG:[]

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        # One median for odd number of number
        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n // 2 + 1)
        # Two median
        smaller = self.findKth(A, 0, B, 0, n // 2)
        bigger = self.findKth(A, 0, B, 0, n // 2 + 1)
        return (smaller + bigger) / 2
        
    # k is the kth number not the actual index
    def findKth(self, A, index_A, B, index_B, k):
        if len(A) == index_A:
            return B[index_B + k - 1]
        if len(B) == index_B:
            return A[index_A + k - 1]
        if k == 1:
            return min(A[index_A], B[index_B])


        a = A[index_A + k // 2 - 1] if index_A + k // 2 <= len(A) else None
        b = B[index_B + k // 2 - 1] if index_B + k // 2 <= len(B) else None

        if b is None or (a is not None and a < b):
            return self.findKth(A, index_A + k // 2, B, index_B, k - k // 2)
        return self. findKth(A, index_A, B, index_B + k // 2, k - k // 2)




























# Takeaways: