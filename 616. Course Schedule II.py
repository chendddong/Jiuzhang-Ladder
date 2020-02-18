'''
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Have you met this question in a real interview?  
Example
Example 1:

Input: n = 2, prerequisites = [[1,0]] 
Output: [0,1]
Example 2:

Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
Output: [0,1,2,3] or [0,2,1,3]
'''

# TAG:[BFS, TOPOLOGY, GRAPH, INDEGREE, CREATE DATA, IMPLICIT GRAPH]

# Solution 1 BFS template

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):        # get indegree
        node_to_indegree, neighbors = self.get_indegree_and_neighbors(numCourses,
           prerequisites)
        # bfs
        queue = collections.deque([node for node in node_to_indegree if node_to_indegree[node] == 0])
        
        # print(neighbors)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            node_to_indegree[node] -= 1

            for neighbor in neighbors[node]:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != numCourses:
            return []

        return order

    def get_indegree_and_neighbors(self, numCourses, prerequisites):
        node_to_indegree = {x : 0 for x in range(numCourses)}
        neighbors = {x : [] for x in range(numCourses)}

        for x, y in prerequisites:
            node_to_indegree[x] += 1
            neighbors[y].append(x)
        return node_to_indegree, neighbors