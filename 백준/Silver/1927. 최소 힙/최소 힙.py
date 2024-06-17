# https://www.acmicpc.net/problem/1927
# 최소 힙

# 못풀었음

import heapq
import sys

input = sys.stdin.read

def main():
    input_data = input().split()
    N = int(input_data[0])
    commands = list(map(int, input_data[1:]))
    
    min_heap = []
    
    for command in commands:
        if command == 0:
            if len(min_heap) == 0:
                print(0)
            else:
                print(heapq.heappop(min_heap))
        else:
            heapq.heappush(min_heap, command)

if __name__ == "__main__":
    main()

