'''
Given a binary tree, design an algorithm which creates a linked list of all
the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

Example 1:

Input: {1,2,3,4}
Output: [1->null,2->3->null,4->null]
Explanation: 
        1
       / \
      2   3
     /
    4
Example 2:

Input: {1,#,2,3}
Output: [1->null,2->null,3->null]
Explanation: 
    1
     \
      2
     /
    3
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

# TAG:[BFS, BINARY TREE, LINKEDLIST, LEVEL ORDER, DFS]

# Solution 1 BFS

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        result = []
        if not root:
            return result

        queue = collections.deque([root])

        dummy = ListNode(sys.maxsize)
        last_node = None

        while queue:
            dummy.next = None
            last_node = dummy
            # on the same level
            for _ in range(len(queue)):
                head = queue.popleft()
                last_node.next = ListNode(head.val)
                last_node = last_node.next

                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)

            result.append(dummy.next)

        return result

# Takeaways
# Go over the algorithm and see the process
# Level order traversal

# Solution 1 DFS Review this after DFS
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        result = []
        self.dfs(root, 1, result)
        return result

    def dfs(self, root, depth, result):
        if not root:
            return

        node = ListNode(root.val)
        if len(result) < depth:
            result.append(node)
        else:
            node.next = result[depth - 1]
            result[depth - 1] = node

        # Because of line 96 and 97 we need to go to the right side first
        self.dfs(root.right, depth + 1, result)
        self.dfs(root.left,  depth + 1, result)

# Takeaways
# Go over the algorithm and see the process



































