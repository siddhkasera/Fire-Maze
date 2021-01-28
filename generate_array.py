import random
import sys


def generate_array(dim: object = 10, p: object = 0.1) -> object:
    # by default, the array will be 10x10 and have a 0.1 probability that the square is blocked
    if (dim<=0):
        print("Dimension must be greater than 0")
        sys.exit()

    arr = [['-'] * dim] * dim
    choices = ['-', 'X']

    if (p <= 0) or (p >= 1):
        print("Please input a probability greater than 0 and less than 1")
        sys.exit()
    else:
        for i in range(len(arr) ):
            arr[i] = random.choices(choices, weights=[1-p, p], k=dim)
        arr[0][0] = 'S'
        arr[dim-1][dim-1] = 'F'
        return arr
