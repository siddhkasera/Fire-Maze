from display_array import display_array
from generate_array import generate_array
from bfs_algo import *
from dfs_algo import *

dim = input("Enter the dimension of the array, in whole numbers: ")
p = input("Enter the probability of each element being filled in, from a range of 0 to 1: ")
arr = generate_array(int(dim), float(p) )

#Note: in Python 3, all inputs are strings for some reason
#insert searches here
while True:
    m = input("Select which algo to use: B for BFS, D for DFS, or All for everything: ")
    if m == 'BFS' or m == 'bfs' or m == 'B' or m == 'b':
        result = bfs(arr, int(dim) )
        display_array(result, int(dim) )
        break
    elif m == 'DFS' or m =='dfs' or m == 'D' or m == 'd':
        #enter DFS here
        pt = Point(0, 0, arr, int(dim), [] )
        pt.dfs(0, 0)
        display_array(arr, int(dim) )
        break
    elif m == "All" or m == "all" or m == "ALL":
        result1 = bfs (arr, int(dim) )
        display_array(result1, int(dim) )
        break
    else:
        print("This is not a valid mode, please try again!")

#print("\nHere is the maze:")
#print("Legend: S = start, - = empty, X = wall, F = finish")
#for row in arr:
#    print(row)
