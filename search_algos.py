
from collections import deque


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def isValid(arr, dim, row, col):
    if (row < 0) or (col < 0) or (row >= dim) or (col >= dim):
        return False
    else:
        return True


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def fillInVisited(arr, dim, visited):
    for i in range(dim):
        for j in range(dim):
            if arr[i][j] == '-' and visited[i][j] == True:
                arr[i][j] = "V"
    return arr


def bfs(arr, dim):
    src = Point(0, 0)
    dest = Point(dim-1, dim-1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True

    queue = deque()  # quicker way to do queue operations
    queue.append(src)

    while queue:

        pt = queue.popleft()  # pop cell

        if pt.x == dest.x and pt.y == dest.y:
            return fillInVisited(arr, dim, visited)

        for i in range(4):
            row = pt.x + dx[i]
            col = pt.y + dy[i]
#evaluate next line when row=1 and col=0
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and (not visited[row][col]):
                # if entry is valid, empty, and not visited
                visited[row][col] = True
                adjCell = Point(row, col)
                queue.append(adjCell)
    # if failure
    print("BFS failed")
    return arr
