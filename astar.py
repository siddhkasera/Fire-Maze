import heapq
from math import sqrt


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class AstarNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt
        self.dist = dist
        self.g = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f


def isValid(arr, dim, row, col):
    if (row < 0) or (col < 0) or (row >= dim) or (col >= dim):
        return False
    else:
        return True


def reconstruct_path(arr, dim, came_from):
    for i in came_from:
        if (i.x != 0 and i.x != 0) or (i.x != dim and i.x != dim):
            arr[i.x][i.y] = "V"
    return arr


def heuristic(a, b):
    """ Calculates the Euclidean Distance between two co-ordinate points """
    z = sqrt(abs(a.x - b.x) ** 2) + sqrt(abs((a.y - b.y) ** 2))

    return z


def astar(arr, dim):
    # direction array
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    src = Point(0, 0)
    dest = Point(dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True

    # setting the g and f values to 0
    src.g = src.f = 0

    open_list = []
    closed_list = []
    came_from = {}
    s = AstarNode(src, 0)
    heapq.heapify(open_list)
    heapq.heappush(open_list, s)

    while len(open_list) > 0:
        current = heapq.heappop(open_list)
        closed_list.append(current)
        pt = current.pt
        if pt.x == dest.x and pt.y == dest.y:  # reached the destination
            print("A* distance: " + str(current.dist))
            return reconstruct_path(arr, dim, came_from)

        for i in range(4):
            row = pt.x + dx[i]
            col = pt.y + dy[i]
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and (not visited[row][col]):
                new_node = AstarNode(row, col)
                neighbor = Point(row, col)
                tent_g = current.g + 1  # calculate tentative g value
                if new_node in closed_list and tent_g >= new_node.g:
                    continue
                if tent_g < new_node.g or new_node not in open_list:
                    came_from[neighbor] = current
                    new_node.g = tent_g
                    new_node.f = tent_g + heuristic(neighbor, dest)
                    new_node.pt = Point(row, col)
                    # pushing the new node in the heap
                    heapq.heappush(open_list, new_node)

    print("Astar failed")
    return arr


def auto_astar(arr, dim):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    src = Point(0, 0)
    dest = Point(dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True

    src.g = src.f = 0

    open_list = []
    closed_list = []
    came_from = {}
    s = AstarNode(src, 0)
    heapq.heapify(open_list)
    heapq.heappush(open_list, s)

    while len(open_list) > 0:
        current = heapq.heappop(open_list)
        closed_list.append(current)
        pt = current.pt
        if pt.x == dest.x and pt.y == dest.y:
            return current.dist

        for i in range(4):
            row = pt.x + dx[i]
            col = pt.y + dy[i]
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and (not visited[row][col]):
                new_node = AstarNode(row, col)
                neighbor = Point(row, col)
                tent_g = current.g + 1
                if new_node in closed_list and tent_g >= new_node.g:
                    continue
                if tent_g < new_node.g or new_node not in open_list:
                    came_from[neighbor] = current
                    new_node.g = tent_g
                    new_node.f = tent_g + heuristic(neighbor, dest)
                    new_node.pt = Point(row, col)
                    heapq.heappush(open_list, new_node)

    print("Astar failed")
    return -1
