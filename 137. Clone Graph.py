'''
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

You need return the node with the same label as the input node.

Have you met this question in a real interview?  
Clarification
How we serialize an undirected graph: http://www.lintcode.com/help/graph/

Example
Example1

Input:
{1,2,4#2,1,4#4,1,2}
Output: 
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2  
 \     |  
  \    |  
   \   |  
    \  |  
      4   
'''

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""


# TAG:[BFS, DEQUE, DEEP COPY, FUNCTIONAL PROGRAMMING, HASHSET, HASHMAP, DFS]
# Solution 1 BFS

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        root = node

        if node is None:
            return node

        # Use BFS to traverse the graph and get all nodes
        nodes = self.getNodes(node)

        # Copy nodes, sotre the old -> new mapping info in a hash map
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # Copy neighbors
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        # return the new graph with the node of the same root
        return mapping[root]

    def getNodes(self, node):

        q = collections.deque([node])
        result = set([node])

        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)

        return result

# Takeaways:
# Must be very familiar with the process of deep copy and how to correctly
# remap the old graph to the new graph. A hash-map can be used to make a copy.

# Solution 2 DFS NEED TO REVIEW LATER

class Solution:

    def __init__(self):
        # a global variable
        self.dict = {}
        
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node is None:
            return None
        
        # exit point
        if node.label in self.dict:
            return self.dict[node.label]
        
        # the new root of the graph
        root = UndirectedGraphNode(node.label)
        self.dict[node.label] = root
        for item in node.neighbors:
            root.neighbors.append(self.cloneGraph(item))

        return root

# Takeaways:
# Need to understand the concept of the DFS








