'''There is a ball in a maze with empty spaces and walls. The ball can go
through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
1.There is only one ball and one destination in the maze.
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
5.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

Example 1:

Input:
map = 
[
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [3,2]
Output:
false
Example 2:

Input:
map = 
[[0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [4,4]
Output:
true
'''
# Solution 1 BFS without visited
# 
# TAG:[BFS]
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        queue = collections.deque([(start[0], start[1])])

        while queue:
            x, y = queue.popleft()
            maze[x][y] = 2
            if (x, y) == (destination[0], destination[1]):
                return True

            for dx, dy in DELTA:
                # Must use a new point we can't change the x, y since it's the
                # starting point
                new_x = x + dx
                new_y = y + dy
                while 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != 1:
                    new_x += dx
                    new_y += dy
                new_x -= dx
                new_y -= dy
                if maze[new_x][new_y] == 0:
                    queue.append((new_x, new_y))

        return False
# Takeaways:
# Thinking about the procedure