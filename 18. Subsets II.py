'''
Given a collection of integers that might contain duplicates, nums, return
all possible subsets (the power set).

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.
Have you met this question in a real interview?  
Example
Example 1:

Input: [0]
Output:
[
  [],
  [0]
]
Example 2:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Challenge
Can you do it in both recursively and iteratively?
'''

# TAG:[DFS, RECURSION]
# Solution 1 DFS
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, index, subset, subsets):
        # print subset
        subsets.append(list(subset))
        # print subsets
        for i in range(index, len(nums)):
            # print("this is level " + str(i))
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()

# Takeaways:
# The thought of the DFS, just try to simulate the process

# Solution 2 non-recursion
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = [[]]
        indices = [-1] # record the indices of the last elements in a subset

        for i in range(len(nums)):
            size = len(subsets)
            for s in range(size):
                if i > 0 and nums[i] == nums[i - 1] and indices[s] != i - 1:
                    continue # trim the duplicates
                subsets.append(list(subsets[s]))
                subsets[-1].append(nums[i])
                indices.append(i)
        return subsets




