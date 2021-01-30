from display_array import display_array
from generate_array import generate_array
from search_algos import *

dim = input("Enter the dimension of the array, in whole numbers: ")
p = input("Enter the probability of each element being filled in, from a range of 0 to 1: ")
arr = generate_array(int(dim), float(p) )
#Note: in Python 3, all inputs are strings
#insert searches here
bfs(arr, int(dim) )
display_array(arr, int(dim) )

#print("\nHere is the maze:")
#print("Legend: S = start, - = empty, X = wall, F = finish")
#for row in arr:
#    print(row)
