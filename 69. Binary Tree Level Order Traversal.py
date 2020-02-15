'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
Have you met this question in a real interview?  
Example
Example 1:

Input：{1,2,3}
Output：[[1],[2,3]]
Explanation：
  1
 / \
2   3
it will be serialized {1,2,3}
level order traversal
Example 2:

Input：{1,#,2,3}
Output：[[1],[2],[3]]
Explanation：
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
level order traversal

Challenge 1: Using only 1 queue to implement it.
Challenge 2: Use BFS algorithm to do it.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# TAG:[BFS, DEQUE, BASICS, COLLECTIONS]
# Solution 1 BFS single queue

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

# add the first node
# while queue
# result for each level
# for every node in the queue
# do popleft() and use it
# go to the next level and add nodes to the queue from left to right
# process the result
# 
# Takeaways:
# queue = collections.deque([root])
# deque's constructor will only allow objects that are iterable to pass
# into the deque()


#   1
#  / \
# 2   3

# queue added node 1
# ----------------
# (1)
# ----------------


# queue has nodes
#     level = []
#     node = (1)(popleft())
#     ----------------

#     ----------------
#     level = [1,]

#     ----------------
#     (2), (3)
#     ----------------
#     result = [[1],]

#     level = []
#     node = (2)(popleft())
#     ----------------
#     (3)
#     ----------------
#     level[2,]
#     node = (3)(popleft())
#     ----------------

#     ----------------
#     level[2, 3]
#     result = [[1], [2,3]]
# queue empty --> out of the loop

# Solution 2 BFS two queues

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        if not root:
            return []

        queue = [root]
        results = []
        while queue:
            next_queue = []
            results.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue # copy might be wasteful if the queue is big
        return results

# Takeaways:
# results.append([node.val for node in queue])

# Solution 3 DFS REVIEW AFTER THE CLASS

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        result = []
        target_level = 0
        while True:
            level = []
            self.dfs(root, 0, target_level, level)
            if not level:
                break
            result.append(level)
            target_level += 1
        return result
        
    def dfs(self, root, cur_level, target_level, level):
        # Corner cases to stop dfs
        if not root or cur_level > target_level:
            return
        if cur_level == target_level:
            level.append(root.val)
        self.dfs(root.left, cur_level + 1, target_level, level)
        self.dfs(root.right, cur_level + 1, target_level, level)
# Takeaways
# Use target_level as an indicator to jump outside of the loop
# when the value of target_level > the level of the B-tree, dfs will stop
