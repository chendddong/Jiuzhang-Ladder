'''
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as
   barrier) with a source position, find the shortest path to a destination position, return the length of the route.
   
Return -1 if destination cannot be reached.

source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.

Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Example
Example 1:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
Example 2:

Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output:-1
'''

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
K_DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]

# TAG:[BFS, HASHMAP, TUPLE, 2D MATRIX, DELTA_X, DELTA_Y, MAXTRIX_IS_VALID]

# Solution 1 BFS

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # Initialization
        queue = collections.deque([(source.x, source.y)])
        # HashMap for distance does two things
        distance = {(source.x, source.y) : 0}

        # BFS
        while queue:
            (x, y) = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for delta_x, delta_y in K_DIRECTIONS:
                next_x, next_y = x + delta_x, y + delta_y
                # duplicates
                if (next_x, next_y) in distance:
                    continue
                # valid
                if not self.is_valid_point(next_x, next_y, grid):
                    continue

                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append(((next_x, next_y)))

        return -1

    # Use sub functions
    def is_valid_point(self, x, y, grid):
        # within boundaries of the grid
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        # can go there
        return not grid[x][y]

# Takeaways:
# 
# HashMap for distance does two things: 1.eliminate duplicate 2.record the ans
# distance = {(source.x, source.y) : 0}
# 
# Use sub functions





































        
