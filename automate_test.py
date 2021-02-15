
from generate_array import generate_array
from bfs_algo import *
from dfs_algo import *
from astar import *
from fire import *
import time
import sys


def automate_test():
    print("AUTOMATED TESTING SCRIPT")
    dim = input("Enter the dimension of the array, in whole numbers: ")
    p = input(
        "Enter the probability of each element being filled in, from a range of 0 to 1: ")
    m = input("Select which mode to use, S for static mazes or F for fire mazes: ")

    if m == "S" or m == "static" or m == "s":
        m = input(
            "Select which algo to use: B for BFS, D for DFS, Aor star for A*:  ")
        num_attempts = input("How many attempts? ")
        file_name = input(
            "Input the name of the file you want to store the output: ")

        print("Performing calculations...")

        num_success = 0
        total_time = 0
        total_dist = 0
        orig_stdout = sys.stdout
        f = open(file_name, "w")
        sys.stdout = f
        print("AUTOMATED TEST RESULT DATA")
        print("Credits: Siddhi Kasera and Em Shi")
        print("Dimension of:", dim)
        print("Density:", p)
        print("Search algo:", m)
        print("--------------")
        for i in range(int(num_attempts)):
            print("\nAttempt ", i)
            if m == 'BFS' or m == 'bfs' or m == 'B' or m == 'b':
                arr = generate_array(int(dim), float(p))
                t0 = time.time()
                r = auto_bfs(arr, int(dim))
                if r > -1:
                    print(r, "steps")
                    num_success = num_success + 1
                    total_dist = total_dist+r
                print(time.time() - t0, "seconds")
                total_time = total_time + time.time() - t0

            elif m == 'DFS' or m == 'dfs' or m == 'D' or m == 'd':
                arr = generate_array(int(dim), float(p))
                t0 = time.time()
                r = auto_dfs(arr, int(dim))
                if r > -1:
                    print(r, "steps")
                    num_success = num_success + 1
                    total_dist = total_dist + r
                print(time.time() - t0, "seconds")
                total_time = total_time + time.time() - t0

            elif m == "Astar" or m == "astar" or m == "A*":
                arr = generate_array(int(dim), float(p))
                t0 = time.time()
                r = auto_astar(arr, int(dim))
                if r > -1:
                    print(r, "steps")
                    num_success = num_success + 1
                    total_dist = total_dist + r
                print(time.time() - t0, "seconds")
                total_time = total_time + time.time() - t0

        print("\n----OVERALL:----")
        print(num_success, "succeeded")
        print("out of", num_attempts, "attempts")
        num_attem = int(num_attempts)
        avg_time = total_time / num_success
        print("The average time taken:", avg_time, "seconds")
        avg_dist = total_dist / num_success
        print("The average distance used:", avg_dist, "units")
        # end file output
        sys.stdout = orig_stdout
        f.close()

        return 0

    elif m == "F" or m == "f" or m == "fire":
        flame = input("Enter a flammability value from a range of 0 to 1: ")
        m = input("Which fire strategy should I use (pick a number 1 to 3), or quit to stop: ")
        num_attempts = input("How many attempts? ")
        file_name = input(
            "Input the name of the file you want to store the output: ")

        print("Performing calculations...")
        orig_stdout = sys.stdout
        f = open(file_name, "w")
        sys.stdout = f

        num_success = 0
        print("AUTOMATED TEST RESULT DATA")
        print("Credits: Siddhi Kasera and Em Shi")
        print("Dimension of:", dim)
        print("Density:", p)
        print("Flammability", flame)
        print("Strategy", m)
        print("--------------")
        for i in range(int(num_attempts)):
            print("\nAttempt ", i)
            if m == "1" or m == "Strategy 1":
                while True:
                    arr = generate_array(int(dim), float(p))
                    if help_dfs(arr, int(dim)) == True:
                        break
                t0 = time.time()
                if strategy1(arr, int(dim), float(flame)):
                    print(time.time() - t0, "seconds")
                    num_success = num_success+1

            elif m == "2" or m == "Strategy 2":
                while True:
                    arr = generate_array(int(dim), float(p))
                    if help_dfs(arr, int(dim)) == True:
                        break
                t0 = time.time()
                if strategy2(arr, int(dim), float(flame)):
                    print(time.time() - t0, "seconds")
                    num_success = num_success+1

            elif m == "3" or m == "Strategy 3":
                while True:
                    arr = generate_array(int(dim), float(p))
                    if help_dfs(arr, int(dim)) == True:
                        break
                t0 = time.time()
                if strategy3(arr, int(dim), float(flame)):
                    print(time.time() - t0, "seconds")
                    num_success = num_success+1

        print("\n----OVERALL:----")
        print(num_success, "succeeded")
        print("out of", num_attempts, "attempts")
        # end file output
        sys.stdout = orig_stdout
        f.close()