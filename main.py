from automate_test import automate_test
from display_array import display_array
from generate_array import generate_array
from bfs_algo import *
from dfs_algo import *
from astar import *
from fire import *
import time

#Rule of thumb: BFS uses the queue and DFS uses the stack. The code is otherwise the same
auto = input("Select if you want to automate a lot of test cases: Y/N: ")
if auto == "Y":
    automate_test()

else:
    m = input("Select which mode to use, S for static mazes or F for fire mazes: ")
    while True:
        if m == "S" or m == "static" or m == "s" or m == "F" or m == "fire" or m == "f" or m == "quit":
            break
        else:
            m = input("Please enter a valid input! S for static mazes or F for fire mazes: ")

    if m == "S" or m == "s" or m == "static":
        dim = input("Enter the dimension of the array, in whole numbers: ")
        p = input("Enter the probability of each element being filled in, from a range of 0 to 1: ")
        arr = generate_array(int(dim), float(p))

        while True:
            m = input(
                "Select which algo to use: B for BFS, D for DFS, Astar for A*, or All for all search algos; or quit to stop: ")
            if m == 'BFS' or m == 'bfs' or m == 'B' or m == 'b':
                t0 = time.time()
                resultB = bfs(arr, int(dim))
                print(time.time() - t0, "seconds")
                # display_array(resultB, int(dim))

            elif m == 'DFS' or m == 'dfs' or m == 'D' or m == 'd':
                t0 = time.time()
                resultD = dfs(arr, int(dim))
                print(time.time() - t0, "seconds")
                # display_array(resultD, int(dim))

            elif m == "All" or m == "all" or m == "ALL":
                t0 = time.time()
                resultB = bfs(arr, int(dim))
                print(time.time() - t0, "seconds")

                t1 = time.time()
                resultD = dfs(arr, int(dim))
                print(time.time() - t1, " seconds")

                t2 = time.time()
                resultA = astar(arr, int(dim))
                print(time.time() - t2, "seconds")

            elif m == "Astar" or m == "astar" or m == "A*":
                t0 = time.time()
                resultA = astar(arr, int(dim))
                print(time.time() - t0, "seconds")
                # display_array(resultA, int(dim))

            elif m == "exit" or m == "quit" or m == "stop":
                break

            else:
                print("This is not a valid mode, please try again!")

    elif m == "F" or m == "f" or m == "fire":
        dim = input("Enter the dimension of the array, in whole numbers: ")
        p = input("Enter the probability of each element being filled in, from a range of 0 to 1: ")
        while True:
            m = input("Which fire strategy should I use (pick a number 1 to 3), or quit to stop: ")
            if m == "1" or m == "Strategy 1":
                f = input("Enter a flammability value from a range of 0 to 1: ")
                arr = generate_array(int(dim), float(p))
                display_array(arr, int(dim))
                t0 = time.time()
                if strategy1(arr, int(dim), float(f)):
                    print(time.time() - t0, "seconds")

            elif m == "2" or m == "Strategy 2":
                f = input("Enter a flammability value from a range of 0 to 1: ")
                arr = generate_array(int(dim), float(p))
                display_array(arr, int(dim))
                t0 = time.time()
                if strategy2(arr, int(dim), float(f)):
                    print(time.time() - t0, "seconds")

            elif m == "exit" or m == "quit" or m == "stop":
                break

            else:
                print("This is not a valid mode, please try again!")



#print("\nHere is the maze:")
#print("Legend: S = start, - = empty, X = wall, F = finish")
#for row in arr:
#    print(row)