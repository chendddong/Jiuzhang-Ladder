'''Given a 2D grid, each cell is either an house 1 or empty 0 (the number zero,
   one), find the place to build a post office, the distance that post office to all the house sum is smallest. Return the smallest distance. Return -1 if it is not possible.
You can pass through house and empty.
You only build post office on an empty.
The distance between house and the post office is Manhattan distance

Problem Correction
Example
Example 1:

Input：[[0,1,0,0],[1,0,1,1],[0,1,0,0]]
Output： 6
Explanation：
Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
Example 2:

Input：[[0,1,0],[1,0,1],[0,1,0]]
Output： 4
Explanation：
Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
'''

# Solution 1 BFS TLE %63
# 
# TAG:[BFS, DELTA, STEPS, LEVEL]
# 
DELTA = [(1, 0),(0, 1),(0, -1),(-1, 0)]

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    # [
    #  [0,1,0,0],
    #  [1,0,1,1],
    #  [0,1,0,0]
    # ]

    # [
    #  [0,1,0,0],
    #  [1,✔️,1,1],
    #  [0,1,0,0]
    # ]    
    def shortestDistance(self, grid):
        n, m = len(grid), len(grid[0])
        ans = sys.maxsize

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    # bfs - The distance from the post office to every house
                    ans = min(ans, self.bfs(grid, i, j))

        return ans

    def bfs(self, grid, x, y):
        queue = collections.deque([(x, y)])
        visited = set((x, y)) # no duplicate allowed

        distance, step = 0, 0
        while queue:
            size = len(queue)
            for _ in range(size):
                now_x, now_y = queue.popleft()

                # Solve problem, because we need result from each level
                if grid[now_x][now_y] == 1:
                    distance += step

                for dx, dy in DELTA:
                    new_x, new_y = now_x + dx, now_y + dy
                    if (new_x, new_y) in visited:
                        continue
                    if not self.is_valid_point(new_x, new_y, grid):
                        continue
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
            step += 1

        return distance

    def is_valid_point(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        return True

# Takeaways:
# DELTA
# USE TUPLE (X, Y)
# ZIP THE DATA n, m = a, b
# SET IS A DICT {}
# ITEM PUT INTO THE DEQUE MUST BE ITERABLE AKA [ITEM]
# THE WAY AND WHEN TO USE STEP
# TEMPLATE OF is_valid_point

# Solution 2 Math 93%
# 
# TAG:[MATH, FORLOOP, AXIS]
# 
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    # [
    #  [0,1,0,0],
    #  [1,0,1,1],
    #  [0,1,0,0]
    # ]

    # [
    #  [0,1,0,0],
    #  [1,✔️,1,1],
    #  [0,1,0,0]
    # ]    
    def shortestDistance(self, grid):
        n, m = len(grid), len(grid[0])
        (house_x, house_y) = self.get_house(grid)
        min_dist = sys.maxsize

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    min_dist = min(min_dist, self.get_dist(i, j, house_x,
                        house_y))

        return min_dist

    def get_house(self, grid):
        n, m = len(grid), len(grid[0])
        (x, y) = [], []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        return (x, y)

    def get_dist(self, i, j, a_x, a_y):
        dis = 0
        for x in a_x:
            dis += abs(i - x)
        for y in a_y:
            dis += abs(j - y)
        return dis

