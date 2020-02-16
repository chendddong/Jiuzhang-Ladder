'''
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

You can assume that there is at least one topological order in the graph.

Clarification
Learn more about representation of graphs

Example
For graph as follow:

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
'''
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

# Solution 1 BFS template
# TAG:[BFS, TOPOLOGICAL, DFS]
# 
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # find indegree for all the nodes
        node_to_indgree = self.get_indegree(graph)

        # bfs search
        order = []
        start_nodes = [n for n in graph if node_to_indgree[n] == 0]
        queue = collections.deque(start_nodes)

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indgree[neighbor] -= 1
                if node_to_indgree[neighbor] == 0:
                    queue.append(neighbor)

        return order

    def get_indegree(self, graph):
        node_to_indgree = {x : 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indgree[neighbor] += 1
        return node_to_indgree

        # node_to_indgree = {}
        # for x in graph:
        #     node_to_indgree[x] = 0

# Takeaways:
# Think about the queue process

# Solution 1 DFS REVISIT AFTER DFS
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        node_to_indgree = self.get_indegree(graph)

        order = []
        for node in graph:
            if node_to_indgree[node] == 0:
                self.dfs(node, node_to_indgree, order)

        return order

    def dfs(self, node, node_to_indgree, order):
        order.append(node)
        node_to_indgree[node] -= 1
        for neighbor in node.neighbors:
            node_to_indgree[neighbor] -= 1
            if node_to_indgree[neighbor] == 0:
                self.dfs(neighbor, node_to_indgree, order)

    def get_indegree(self, graph):
        node_to_indgree = {x : 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indgree[neighbor] += 1
        return node_to_indgree


# Takeaways:
# Create usable functions




















































        
