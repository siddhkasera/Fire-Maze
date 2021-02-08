from display_array import display_array
from generate_array import generate_array
from bfs_algo import *
from dfs_algo import *
from astar import *
from fire import *
import time

#Rule of thumb: BFS uses the queue and DFS uses the stack. The code is otherwise the same

dim = input("Enter the dimension of the array, in whole numbers: ")
p = input("Enter the probability of each element being filled in, from a range of 0 to 1: ")
arr = generate_array(int(dim), float(p) )
f = input("Enter a flammability value from a range of 0 to 1: ")

#Note: in Python 3, all inputs are strings for some reason
#insert searches here
while True:
    s = input("Select whether to test for search algos or fires: S for search and F for fire, or exit to quit: ")
    if s == 'S' or s == 's' or s == "search":
        while True:
            m = input("Select which algo to use: B for BFS, D for DFS, Astar for A*, or All for all search algos: ")
            if m == 'BFS' or m == 'bfs' or m == 'B' or m == 'b':
                t0 = time.time()
                resultB = bfs(arr, int(dim))
                print(time.time() - t0, "seconds")
                display_array(resultB, int(dim))
                break
            elif m == 'DFS' or m == 'dfs' or m == 'D' or m == 'd':
                t0 = time.time()
                resultD = dfs(arr, int(dim))
                print(time.time() - t0, "seconds")
                display_array(resultD, int(dim))
                break
            elif m == "All" or m == "all" or m == "ALL":
                t0 = time.time()
                resultB = bfs(arr, int(dim))
                print(time.time() - t0, "seconds")

                t1 = time.time()
                resultD = dfs(arr, int(dim))
                print(time.time() - t1, " seconds")

                t2 = time.time()
                resultA = a_star(arr, int(dim))
                print(time.time() - t2, "seconds")
                break

            elif m == "Astar" or m == "astar" or m == "A*":
                t0 = time.time()
                result = a_star(arr, int(dim))
                print(time.time() - t0, "seconds")
                display_array(result, int(dim))
                break

            else:
                print("This is not a valid mode, please try again!")

            break

    elif s == 'f' or s == 'F' or s == "Fire":
        while True:
            m = input("Which fire strategy should I use (pick a number from 1 to 3): ")
            if m == '1' or m == "Strategy 1":
                t0 = time.time()
                if strategy1(arr, int(dim), float(f) ) == True:
                    print(time.time() - t0, "seconds")
                break
            break

    elif s == "exit" or s == "quit" or s == "Exit" or s == "Quit":
        break

    else:
        print("This is not a valid input")

#print("\nHere is the maze:")
#print("Legend: S = start, - = empty, X = wall, F = finish")
#for row in arr:
#    print(row)
