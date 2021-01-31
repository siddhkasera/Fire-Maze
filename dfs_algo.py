class Point:
    def __init__(self, x: int, y: int, arr, dim, visited):
        self.x = x
        self.y = y
        self.arr = arr
        self.dim = dim
        self.visited = visited

    def isValid(self, x, y, visited):
        if x < 1 or x > self.dim-1:
            return False
        elif y < 1 or y > self.dim-1:
            return False
        elif visited[x][y] is True:
            return False
        else:
            return True

    # def _visited(self, visited):

    def dfs(self, x, y):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        count = 0

        for i in range(4):

            if self.isValid(x + dx[i], y + dy[i], self.visited) and self.arr[x + dx[i][dy + i]] != 'X':
                count = count + 1
                self.visited[x + dx[i]][y + dy[i]] = True
                self.dfs(x + dx[i], y + dy[i])
