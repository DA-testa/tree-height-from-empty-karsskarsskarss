# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Write this function
    tree = [[] for _ in range(n)]
    root = 0
    
    # max_height = 0
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = 1
        else:
            tree[parent].append(i)

   # return max(depth)

    def height(node):
        if not tree[node]:
            return 1
        return 1 + max(height(child)for child in tree[node])
    return height (root) 

def main():
    n = int(input().strip())
    parents = list(map(int, input().strip().split()))
    height = compute_height(n, parents)#koka augstumu
    print(height)#izvada rez

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)  
threading.Thread(target=main).start()
#main()

#print(numpy.array([1,2,3]))