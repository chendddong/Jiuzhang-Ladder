'''
There is a ball in a maze with empty spaces and walls. The ball can go
through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

1.There is only one ball and one destination in the maze.
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
4.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

Example 1:
    Input:  
    (rowStart, colStart) = (0,4)
    (rowDest, colDest)= (4,4)
    0 0 1 0 0
    0 0 0 0 0
    0 0 0 1 0
    1 1 0 1 1
    0 0 0 0 0

    Output:  12
    
    Explanation:
    (0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)

Example 2:
    Input:
    (rowStart, colStart) = (0,4)
    (rowDest, colDest)= (0,0)
    0 0 1 0 0
    0 0 0 0 0
    0 0 0 1 0
    1 1 0 1 1
    0 0 0 0 0

    Output:  6
    
    Explanation:
    (0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(0,0)
'''

# Solution 1 BFS
# 
# TAG:[BFS, STRING, BACKTRACKING, DFS]
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # array -> tuple
        start = (start[0], start[1])
        destination = (destination[0], destination[1])

        # added as a tuple in a list, the next append just need a tuple
        queue = collections.deque([start]) 
        # added as a tuple, the next add just need a tuple
        visited = {start : 0}

        while queue:
            point = queue.popleft()
            new_points = self.get_new_points(point, maze, visited)
            for next_point in new_points:
                # update the steps if it's smaller
                if next_point in visited:
                    if new_points[next_point] < visited[next_point]:
                        visited[next_point] = new_points[next_point]
                else:
                    # not visited point pushed into queue
                    queue.append(next_point)
                    # recorded new point steps in visited
                    visited[next_point] = new_points[next_point]

        if destination in visited:
            return visited[destination]

        return -1

    def get_new_points(self, point, maze, visited):
        points = {}
        m, n = len(maze), len(maze[0])

        # Go to the furtherest point it can go until it got stopped from 4
        # directions
        for dx, dy in DELTA:
            x, y = point
            count = -1
            while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                x += dx
                y += dy
                count += 1
                # When stopped by something, record the previous point
            points[(x - dx, y - dy)] = visited[point] + count

        return points
# Takeaways:
# 1. SET:
# -------------------------
#       a = set([(1, 2)])
#       a.add((2,4))
#       a: {(1, 2), (2, 4)}
# -------------------------
#       a = set((1, 2))
#       a.add((2, 4))
#       a: {1, 2, (2, 4)}
# -------------------------
# 2. Deque(queue):
# -------------------------
#       queue = collections.deque([(1, 2)])
#       queue.append((2, 3))
#       queue: deque([(1, 2), (2, 3)])
# -------------------------
#       queue = collections.deque((1, 2))
#       queue.append((2, 3))
#       queue: deque([1, 2, (2, 3)])
# -------------------------
# 
# Conclusion: always use the [] when initialize the set or deque. The element
# added later would be the data type.


# Solution 2 DFS REVIEW AFTER DFS 
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        paths = []
        start = (start[0], start[1])
        destination = (destination[0], destination[1])
        visited = set([start])

        self.dfs(maze, start, destination, 0, visited, paths)
        if len(paths) == 0:
            return -1
        return min(paths)

    def dfs(self, maze, start, destination, step, visited, paths):
        if start == destination:
            paths.append(step)
            return
        # no parenthesis to loop a tuple
        for dx, dy in DELTA:
            (x, y) = start
            starting_step = step
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                x += dx
                y += dy
                starting_step += 1 # go forward
            x -= dx
            y -= dy
            starting_step -= 1 # step back one steps if encounters objects

            if (x, y) not in visited:
                visited.add((x, y))
                self.dfs(maze, (x, y), destination, starting_step, visited,
                    paths)
                visited.remove((x, y))

# Takeaway:
# why back tracking?
# when back tracking?
# the way to construct DFS or recursion























