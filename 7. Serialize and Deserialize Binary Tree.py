'''
Design an algorithm and write code to serialize and deserialize a binary
tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.

Example
Example 1:

Input：{3,9,20,#,#,15,7}
Output：{3,9,20,#,#,15,7}
Explanation：
Binary tree {3,9,20,#,#,15,7},  denote the following structure:
      3
     / \
    9  20
      /  \
     15   7
it will be serialized {3,9,20,#,#,15,7}
Example 2:

Input：{1,2,3}
Output：{1,2,3}
Explanation：
Binary tree {1,2,3},  denote the following structure:
   1
  / \
 2   3
it will be serialized {1,2,3}
Our data serialization use BFS traversal. This is just for when you got Wrong Answer and want to debug the input.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# TAG:[BFS, DEQUE, TRIM, STRING, STRIP, SPLIT]
# Solution 1 BFS single queue

class Solution:

    def serialize(self, root):

        
        if root is None:
            return "{}"

        queue = collections.deque([root])
        level = 0

        while level < len(queue):
            if queue[level] is not None:
                queue.append(queue[level].left)
                queue.append(queue[level].right)
            level += 1

        # trim the # at the end
        while queue[-1] is None:
            queue.pop()

        # string manipulation
        return '{%s}' % ','.join([str(node.val) if node is not None else '#'
            for node in queue])

    def deserialize(self, data):
        # clean the data
        data = data.strip('\n')

        if data == '{}':
            return None

        # convert the whole string to elements in a list
        # "{1,2,3}"  --> ["1", "2", "3"]
        vals = data[1:-1].split(',')

        root = TreeNode(int(vals[0]))
        queue = collections.deque([root])
        isLeftChild = True
        index = 0
 
        # use index as the level connecting all the nodes together
        # Since we use "#", we can use isLeftChild as a flag 
        for val in vals[1:]:
            if val is not "#":
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild

        return root