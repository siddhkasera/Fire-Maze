import heapq


# create a prority queue class.
# create a heuristic function.

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class AStarNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt
        self.dist = dist


def isValid(arr, dim, row, col):
    if (row < 0) or (col < 0) or (row >= dim) or (col >= dim):
        return False
    else:
        return True


def heuristic(a, b):
    """ Calculates the Manhantan Distance between two co-ordinate points """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def fillInVisited(arr, dim, visited):
    for i in range(dim):
        for j in range(dim):
            if arr[i][j] == '-' and visited[i][j] == True:
                arr[i][j] = "V"
    return arr


def a_star(arr, dim):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    src = (0, 0)
    dest = (dim - 1, dim - 1)
    # src = (0, 0)
    # dest = (dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True

    pq = PriorityQueue()
    pq.put(src, 0)
    g_values = {src: 0}

    while not pq.is_empty():
        current = pq.get()  # pop the cell coordinates
        if current == dest:
            #print("AStar distance:" + cor.dist)
            return fillInVisited(arr, dim, visited)
        for i in range(4):
            row = current[0] + dx[i]
            col = current[1] + dy[i]
            neighbor = (row, col)
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and neighbor not in g_values:
                new_cost = g_values[current] + 1
                g_values[neighbor] = new_cost
                f_value = new_cost + heuristic(dest, neighbor)
                #adj = AStarNode(Point(row, col), cor.dist + 1)
                visited[row][col] = True
                pq.put(neighbor, f_value)

    print("A-star failed")
    return arr
