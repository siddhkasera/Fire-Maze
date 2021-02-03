import heapq

# create a prority queue class.
# create a heuristic function.
from math import sqrt
from typing import Any, Union


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __iter__(self):
        return self

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
    """ Calculates the Euclidean Distance between two co-ordinate points """
    x1, y1 = a
    x2, y2 = b
    return sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)


def fillInVisited(arr, dim, visited):
    for i in range(dim):
        for j in range(dim):
            if arr[i][j] == '-' and visited[i][j] == True:
                arr[i][j] = "V"
    return arr


def a_star(arr, dim):
    # direction array
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    src = (0, 0)
    dest = (dim - 1, dim - 1)
    # src = (0, 0)
    # dest = (dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True

    # pq = PriorityQueue()

    closed_set = set()
    came_from = {}
    # pq.put(src, 0)  # first coordinate with priority 0 added in the queue.
    # g-value: best distance from start to current cell
    g_values = {src: 0}  #
    f_values = {}
    pq = []

    heapq.heappush(pq, (f_values[src], src))

    while pq:
        current = heapq.heappop(pq)[1]  # pop the cell coordinates
        if current == dest:
            # print("AStar distance:" + cor.dist)
            path = []
            while current in came_from:
                path.append(current)  # Gscore[neighbor]
                current = came_from[current]
            # return fillInVisited(arr, dim, visited)
            return path
        for i in range(4):
            row = current[0] + dx[i]
            col = current[1] + dy[i]
            neighbor = (row, col)
            tent_g_value = g_values[current] + heuristic(current, neighbor)
            if isValid(arr, dim, row, col) and arr[row][col] != 'X':
                if neighbor in closed_set and tent_g_value >= g_values.get(neighbor, 0):
                    continue
                if tent_g_value < g_values.get(neighbor, 0) or neighbor not in [i[1] for i in pq]:
                    came_from[neighbor] = current
                    g_values[neighbor] = tent_g_value
                    f_values[neighbor] = tent_g_value + heuristic(neighbor, dest)
                    #visited[row][col] = True
                    heapq.heappush(pq, (f_values[neighbor], neighbor))

                # adj = AStarNode(Point(row, col), cor.dist + 1)
    print("A-star failed")
    return arr
# 0.1 -0.3 run the algo on 50 diff mazezs. how many of you were able to find the path divided by total
# generate 50 mazes with a one probability. total no times you found the path/ total no of times you ran the alfo.
