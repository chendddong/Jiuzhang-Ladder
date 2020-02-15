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

# TAG:[BFS, TOPOLOGY, GRAPH, INDEGREE]
# 
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        node_to_indegree = self.get_indegree(numCourses, prerequisites)
        
        neighbors = {i : [] for i in range(numCourses)}
        for x, y in prerequisites:
            neighbors[y].append(x)
        
        start_nodes = [i for i in range(numCourses) if node_to_indegree[i] == 0]
        
        queue = collections.deque(start_nodes)
        
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in neighbors[node]:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) != numCourses:
            return []
        
        return order
    
    def get_indegree(self, numCourses, prerequisites):
        node_to_indegree = {i : 0 for i in range(numCourses)}
        
        for x, y in prerequisites:
            node_to_indegree[x] += 1
        
        return node_to_indegree
        