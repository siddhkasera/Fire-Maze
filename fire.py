import random
from heapq import *

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


def setFire(arr, dim):
    while True:
        randX = random.randint(0, dim)
        randY = random.randint(0, dim)

        # check if cell is valid and empty
        if isValid(arr, dim, randX, randY) == True and arr[randX][randY] == '-':
            arr[randX][randY] = 'F'
            break

    return arr


def spreadFire(arr, dim, flammability):
    copyArr = arr  # if I don't use a copy, I will get a 100% fire maze in 1 step :(
    for x in range(dim):
        for y in range(dim):
            if arr[x][y] == '-':  # if not fire
                k = 0  # number of fire neighbors
                dx = [-1, 0, 0, 1]
                dy = [0, -1, 1, 0]
                for i in range(4):
                    neighX = dx[i] + x
                    neighY = dy[i] + y
                    if isValid(arr, dim, neighX, neighY) == True and arr[neighX][neighY] == 'F':
                        k = k + 1
                prob = 1 - (1 - flammability) ** k
                rand = random.randint(0, 100) / 100

                if rand < prob:
                    copyArr[x][y] = 'F'

    return copyArr


def help_dfs(arr, dim):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    src = Point(0, 0)
    dest = Point(dim - 1, dim - 1)

    v = [[False for i in range(dim)] for j in range(dim)]
    v[0][0] = True
    stack = []
    s = StackNode(src, 0)
    stack.append(s)

    while stack:
        current = stack.pop(len(stack) - 1)
        pt = current.pt
        if pt.x == dest.x and pt.y == dest.y:
            return True
        for i in range(4):
            row = pt.x + dx[i]
            col = pt.y + dy[i]
            # evaluate next line when row=1 and col=0
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and (not v[row][col]):
                # if entry is valid, empty, and not visited
                v[row][col] = True
                adjCell = StackNode(Point(row, col), current.dist + 1)
                stack.append(adjCell)

    return False


def strategy1(arr, dim, flammability):
    # This strategy is the exact same as a search algo, very naive and will not take into account fires
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    src = Point(0, 0)
    dest = Point(dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True
    stack = []
    s = StackNode(src, 0)
    stack.append(s)

    if help_dfs(arr, dim) == False:
        print("No path from start to goal")
        return False

    setFire(arr, dim)

    while stack:
        current = stack.pop(len(stack) - 1)
        pt = current.pt
        arr = spreadFire(arr, dim, flammability)
        # I interpreted the directions as "for every step, do spreadFire()"
        if arr[pt.x][pt.y] == 'F':
            print("Agent burned before reaching the goal")
            return False
        if pt.x == dest.x and pt.y == dest.y:
            print("Success!")
            return True
        for i in range(4):
            row = pt.x + dx[i]
            col = pt.y + dy[i]
            # evaluate next line when row=1 and col=0
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and (not visited[row][col]):
                # if entry is valid, empty, and not visited
                visited[row][col] = True
                adjCell = StackNode(Point(row, col), current.dist + 1)
                stack.append(adjCell)

    print("No path from start to goal - surrounded by fire")
    return False


def strategy2(arr, dim, flammability):
    # This strategy now considers fire as a wall
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    src = Point(0, 0)
    dest = Point(dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True
    stack = []
    s = StackNode(src, 0)
    stack.append(s)

    if help_dfs(arr, dim) == False:
        print("No path from start to goal")
        return False

    setFire(arr, dim)

    while stack:
        current = stack.pop(len(stack) - 1)
        pt = current.pt
        arr = spreadFire(arr, dim, flammability)
        # I interpreted the directions as "for every step, do spreadFire()"
        if arr[pt.x][pt.y] == 'F':
            print("Agent burned before reaching the goal")
            return False
        if pt.x == dest.x and pt.y == dest.y:
            print("Success!")
            return True
        for i in range(4):
            row = pt.x + dx[i]
            col = pt.y + dy[i]
            # evaluate next line when row=1 and col=0
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and arr[row][col] != 'F' and (
                    not visited[row][col]):
                # if entry is valid, empty, and not visited
                visited[row][col] = True
                adjCell = StackNode(Point(row, col), current.dist + 1)
                stack.append(adjCell)

    print("No path from start to goal - surrounded by fire")
    return False


######################################################################################
class PqNode:
    def __init__(self, pt: Point, dist: float):
        self.pt = pt
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist

    def __gt__(self, other):
        return self.dist > other.dist


def minFire(arr, dim, pt):
    minDistance = dim*dim

    for i in range(dim):
        for j in range(dim):
            if arr[i][j] == "F":
                dist = fireDfs(arr, dim, pt, Point(i, j) )
                if -1 < dist < minDistance: # -1 means failed, and then distance must be positive
                    minDistance = dist

    return minDistance


def fireDfs(arr, dim, a, b):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    src = Point(a.x, a.y)
    dest = Point(b.x, b.y)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True
    stack = []
    s = StackNode(src, 0)
    stack.append(s)

    while stack:
        current = stack.pop(len(stack) - 1)
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
                adjCell = StackNode(Point(row, col), current.dist + 1)
                stack.append(adjCell)

    # No path found from fire to start point, test failed
    return -1


def strat3heuristic(arr, dim, a, b):
    # The formula: distance to destination - (alpha * smallest distance from fire), and select the smallest

    alpha = 0.5  # This value can be changed

    m = minFire(arr, dim, a)

    z = abs(a.x - b.x) + abs(a.y - b.y)  # Using Manhattan distance
    return z-(alpha*m)


def strategy3(arr, dim, flammability):
    # THE STRATEGY
    # Do the exact same thing as DFS except:
    # -instead of a stack, use a priority queue
    # -the priority will be decided using the following formula:
    #   distance to destination - (alpha * smallest distance from fire), and select the smallest
    #

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    src = Point(0, 0)
    dest = Point(dim - 1, dim - 1)

    visited = [[False for i in range(dim)] for j in range(dim)]
    visited[0][0] = True

    if help_dfs(arr, dim) == False:
        print("No path from start to goal")
        return False

    setFire(arr, dim)
    heap = []
    heappush(heap, PqNode(src, strat3heuristic(arr, dim, src, dest) ) )

    while heap:
        current = heappop(heap)
        pt = current.pt
        arr = spreadFire(arr, dim, flammability)
        if arr[pt.x][pt.y] == 'F':
            print("Agent burned before reaching the goal")
            return False
        if pt.x == dest.x and pt.y == dest.y:
            print("Success!")
            return True
        for i in range(4):
            row = pt.x + dx[i]
            col = pt.y + dy[i]
            # evaluate next line when row=1 and col=0
            if isValid(arr, dim, row, col) and arr[row][col] != 'X' and arr[row][col] != 'F' and (
                    not visited[row][col]):
                # if entry is valid, empty, and not visited
                visited[row][col] = True
                adjPt = Point(row, col)
                heappush(heap, PqNode(adjPt, strat3heuristic(arr, dim, adjPt, dest) ) )

    print("No path from start to goal - surrounded by fire")
    return False
