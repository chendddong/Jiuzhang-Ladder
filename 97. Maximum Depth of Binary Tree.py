'''Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
The answer will not exceed 5000
Example
Example 1:

Input: tree = {}
Output: 0
Explanation: The height of empty tree is 0.
Example 2:

Input: tree = {1,2,3,#,#,4,5}
Output: 3   
Explanation: Like this:
   1
  / \                
 2   3                
    / \                
   4   5
it will be serialized {1,2,3,#,#,4,5}
'''

# TAG:[Traverse, Recursion, Non-Recursion, BFS]

# Solution 1 Traverse -- Global Variable
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        self.depth = 0
        self.traverse(root, 1)
        return self.depth

    def traverse(self, root, cur_depth):
        if not root:
            return

        self.depth = max(self.depth, cur_depth)
        self.traverse(root.left, cur_depth + 1)
        self.traverse(root.right, cur_depth + 1)


# Solution 2 D&C 
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

# Solution 3 BFS
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        if not root:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth

# Takeaways:
# Solution 1: When accessing global variable, use self.stuff everywhere!
# Solution 2: There will be some return values.
# Solution 3: Only the level matters. Use range(len(queue)) !!!
 