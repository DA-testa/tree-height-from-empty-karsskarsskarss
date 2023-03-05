# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
    depth = [0] * n
    # max_height = 0
    for i in range(n):
        if parents[i] == -1:
            depth[i] = 1
        else:
            depth[i] = depth[parents[i]] + 1

    return max(depth)
#creed3

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    height = compute_height(n, parents)
    print(height)

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)  
threading.Thread(target=main).start()
main()

print(numpy.array([1,2,3]))