
from generate_array import generate_array
from auto_bfs import *
from auto_dfs import *
from auto_astar import *
from fire import *
import time
import sys


def automate_test():
    print("AUTOMATED TESTING SCRIPT")
    dim = input("Enter the dimension of the array, in whole numbers: ")
    p = input("Enter the probability of each element being filled in, from a range of 0 to 1: ")
    m = input("Select which mode to use, S for static mazes or F for fire mazes: ")

    if m == "S" or m == "static" or m == "s":
        m = input(
            "Select which algo to use: B for BFS, D for DFS, Aor star for A*:  ")
        num_attempts = input("How many attempts? ")
        file_name = input("Input the name of the file you want to store the output: ")

        num_success = 0

        orig_stdout = sys.stdout
        f = open(file_name, "w")
        sys.stdout = f
        print("AUTOMATED TEST RESULT DATA")
        print("Credits: Siddhi Kasera and Em Shi")
        print("Dimension of:", dim)
        print("Density:", p)
        print("Search algo:", m)
        print("--------------")
        for i in range(int(num_attempts) ):
            print("\nAttempt " , i)
            if m == 'BFS' or m == 'bfs' or m == 'B' or m == 'b':
                arr = generate_array(int(dim), float(p))
                t0 = time.time()
                r = auto_bfs(arr, int(dim))
                if (r > -1):
                    print(r , "steps")
                    num_success = num_success+1
                print(time.time() - t0, "seconds")

            elif m == 'DFS' or m == 'dfs' or m == 'D' or m == 'd':
                arr = generate_array(int(dim), float(p))
                t0 = time.time()
                r = auto_dfs(arr, int(dim))
                if (r > -1):
                    print(r, "steps")
                    num_success = num_success + 1
                print(time.time() - t0, "seconds")

            elif m == "Astar" or m == "astar" or m == "A*":
                arr = generate_array(int(dim), float(p))
                t0 = time.time()
                r = auto_astar(arr, int(dim))
                if (r > -1):
                    print(r, "steps")
                    num_success = num_success + 1
                print(time.time() - t0, "seconds")

        print("\n----OVERALL:----")
        print(num_success, "succeeded")
        print("out of", num_attempts, "attempts")
        #end file output
        sys.stdout = orig_stdout
        f.close()

        return 0