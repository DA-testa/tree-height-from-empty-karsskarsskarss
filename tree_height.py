#Artūrs Jānis Karss IT 1. grupa
import sys

def compute_height(n, parents):
    height = [0] * n
    max_height = 0
    
    for i in range(n):
        if height[i] == 0:
            node = i
            depth = 0
            while node != -1:
                if height[node] != 0:
                    depth += height[node]
                    break
                depth += 1
                node = parents[node]
            max_height = max(max_height, depth)
            node = i
            while node != -1:
                if height[node] != 0:
                    break
                height[node] = depth
                depth -= 1
                node = parents[node]
    
    return max_height

def main():
    text = input().strip()
    if text == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    elif text == "F":
        filename = input().strip()
        with open(f"test/{filename}", "r") as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    else:
        print("Invalid input format.")
        return
    print(compute_height(n, parents))

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    main()
