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
    input_type = input("Input type (K for keyboard, F for file): ").strip().upper()

    if input_type == "K":
        n = int(input("Enter number of nodes: ").strip())
        parents = list(map(int, input("Enter parent indices separated by spaces: ").strip().split()))
    elif input_type == "F":
        file_name = input("Enter file name: ").strip()
        if 'a' in file_name:
            print("Invalid file name. Please enter a different file name.")
            return
        try:
            with open(f"folder/{file_name}") as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")
            return
    else:
        print("Invalid input type. Please enter K or F.")
        return

    height = compute_height(n, parents)
    print(height)

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)  
threading.Thread(target=main).start()
#main()


