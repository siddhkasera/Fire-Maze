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

    # def get_pos(self):
    #    return self.x, self.y
    def __iter__(self):
        return self

    def __next__(self):
        for i in Point:
            return self.__getattribute__(i)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


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
    print("values in a and b inside heuristic are:")
    print(a.x, a.y)
    print(b.x, b.y)
    z = sqrt(a.x - b.x) ** 2 + abs(a.y - b.y) ** 2
    print("H value is")
    print(z)
    return z


def fillInVisited(arr, dim, visited):
    for i in range(dim):
        for j in range(dim):
            if arr[i][j] == '-' and visited[i][j] == True:
                arr[i][j] = "V"
    return arr


def reconstruct_path(arr, came_from, current):
    while current in came_from:
        current = came_from[current]
        i = current.x
        j = current.y
        arr[i][j] = "V"
    return arr


def a_star(arr, dim):
    # direction array
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    src = Point(0, 0)
    dest = Point(dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True
    closed_set = set()
    came_from = {}
    # pq.put(src, 0)  # first coordinate with priority 0 added in the queue.
    # g-value: best distance from start to current cell
    g_values = {Point: float("inf") for dim in arr for Point in dim}
    g_values[src] = 0
    f_values = {Point: float("inf") for dim in arr for Point in dim}
    f_values[src] = heuristic(src, dest)
    print("The f_values:")
    print(f_values)
    pq = []

    heapq.heappush(pq, (f_values[src], src))
    # ___hash___()
    # __eq___()
    # Making python class usable as dictionary key
    while pq:
        current = heapq.heappop(pq)[1]  # pop the cell coordinates
        if current.x == dest.x:
            return reconstruct_path(arr, current, came_from)
        for i in range(4):
            row = current.x + dx[i]
            col = current.y + dy[i]
            if isValid(arr, dim, row, col) and arr[row][col] != 'X':
                neighbor = Point(row, col)
                tent_g_value = g_values[current] + 1
                if neighbor in closed_set and tent_g_value >= g_values.get(neighbor, 0):
                    continue
                if tent_g_value < g_values.get(neighbor, 0) or neighbor not in [i[1] for i in pq]:
                    came_from[neighbor] = current
                    g_values[neighbor] = tent_g_value
                    f_values[neighbor] = tent_g_value + heuristic(neighbor, dest)
                    heapq.heappush(pq, (f_values[neighbor], neighbor))
            #if current != src:
             #   closed_set.add(current)
    print("A-star failed")
    return arr
# 0.1 -0.3 run the algo on 50 diff mazezs. how many of you were able to find the path divided by total
# generate 50 mazes with a one probability. total no times you found the path/ total no of times you ran the alfo.
