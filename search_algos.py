
class search_algos:

    def __init__(self, arr, dim): #the first param in the function will call this instance of the class
        self.arr = arr
        self.dim = dim
        self.queue = [] #for BFS

    def is_valid(self, x, y): #check validity of given X and Y
        if (x >= self.dim) or (y >= self.dim):
            return "No"
        elif (x < 0) or (y < 0):
            return "No"
        elif self.arr[x][y] == 'X': #wall found
            return "No"
        elif (x == 0) and (y == 0):
            return "Start"
        elif (x == self.dim-1) and (y == self.dim-1):
            return "Finish"
        else:
            return "Yes"
    #use "V" to mark visited

    def bfs(self, x, y):
        #direction vectors
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        #push onto queue
        self.queue.append( [x, y] )
        while self.queue != []:
            #as long as queue is filled with something, loop continues
            current = self.queue.pop()

            if self.is_valid(current[0], current[1]) == "Finish":
                break
            for i in range(4):
                nextX = current[0]+dx[i]
                nextY = current[1]+dy[i]
                if self.is_valid(nextX, nextY) == "No":
                    continue
                else:#bug is somewhere here, I think
                    self.queue.append( [nextX, nextY] )
                    if (nextX != self.dim-1) and (nextY != self.dim-1) and (self.is_valid(nextX, nextY) == 'Yes'):
                        self.arr[nextX][nextY] = 'V'
                    elif self.is_valid(nextX, nextY) == "Finish":
                        break
        return self.arr