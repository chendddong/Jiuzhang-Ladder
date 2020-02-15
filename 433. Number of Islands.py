'''
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as
the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Example 1:

Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
Example 2:

Input:
[
  [1,1]
]
Output:
1
'''

# TAG:[BFS, 2D MATRIX, DELTA_X, DELTA_Y, MAXTRIX_IS_VALID, *DFS]
# 
# Solution 1 BFS Template (recommended solution)
# 
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # corner cases
        if not grid or not grid[0]:
            return 0

        islands = 0
        visited = set() # Convenient feature of python

        # traverse the matrix and update the number of island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1

        return islands

    def bfs(self, grid, x, y, visited):
        # use tuple to simplify the 2D matrix bfs process
        queue = collections.deque([(x, y)])
        # visited and queue are best buddies
        visited.add((x, y)) 

        while queue:
            x, y = queue.popleft()
            # way to traverse the adjacent nodes
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        # within range
        if not (0 <= x < n and 0 <= y < m):
            return False
        # visited?
        if (x, y) in visited:
            return False
        # island?
        return grid[x][y]

# Takeaways:
# use tuple to simplify the 2D matrix bfs process
# 
# way to traverse the adjacent nodes
# for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
#               next_x = x + delta_x
#               next_y = y + delta_y
# 
# is_valid:
#   within range?
#   visited?
#   island?

# Solution 2 DFS not recommended. REVIEW AGAIN FOR DFS

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        self.n, self.m = len(grid), len(grid[0])
        self.visited = [[False] * self.m for _ in range(self.n)]
        
        islands = 0
        for row in range(self.n):
            for col in range(self.m):
                if self.is_island(grid, row, col):
                    self.visited[row][col] = True
                    self.dfs(grid, row, col)
                    islands += 1
                    
        return islands
        
    def is_island(self, grid, x, y):
        return 0 <= x < self.n and 0 <= y < self.m and grid[x][y] and not self.visited[x][y]

    def dfs(self, grid, x, y):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for direction in range(4):
            newx = x + dx[direction]
            newy = y + dy[direction]
            
            if self.is_island(grid, newx, newy):
                self.visited[newx][newy] = True
                self.dfs(grid, newx, newy)