class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class StackNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt
        self.dist = dist


def isValid(arr, dim, row, col):
    if (row < 0) or (col < 0) or (row >= dim) or (col >= dim):
        return False
    else:
        return True


def fillInVisited(arr, dim, visited):
    for i in range(dim):
        for j in range(dim):
            if arr[i][j] == '-' and visited[i][j] == True:
                arr[i][j] = "V"
    return arr


def dfs(arr, dim):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    src = Point(0, 0)
    dest = Point(dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True
    stack = []
    s = StackNode(src, 0)
    stack.append(s)

    while stack:
        current = stack.pop(len(stack)-1)
        pt = current.pt
        if pt.x == dest.x and pt.y == dest.y:
            print("DFS distance: " + str(current.dist) )
            return fillInVisited(arr, dim, visited)
        for i in range(4):
            row = pt.x + dx[i]
            col = pt.y + dy[i]
            # evaluate next line when row=1 and col=0
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and (not visited[row][col]):
                # if entry is valid, empty, and not visited
                visited[row][col] = True
                adjCell = StackNode(Point(row, col), current.dist+1)
                stack.append(adjCell)

    print("DFS failed")
    return arr


def auto_dfs(arr, dim):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    src = Point(0, 0)
    dest = Point(dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True
    stack = []
    s = StackNode(src, 0)
    stack.append(s)

    while stack:
        current = stack.pop(len(stack)-1)
        pt = current.pt
        if pt.x == dest.x and pt.y == dest.y:
            return current.dist
        for i in range(4):
            row = pt.x + dx[i]
            col = pt.y + dy[i]
            # evaluate next line when row=1 and col=0
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and (not visited[row][col]):
                # if entry is valid, empty, and not visited
                visited[row][col] = True
                adjCell = StackNode(Point(row, col), current.dist+1)
                stack.append(adjCell)

    print("DFS failed")
    return -1