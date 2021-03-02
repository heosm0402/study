import heapq
import sys

N = int(input())

heap = []
for _ in range(N):
    comm = int(sys.stdin.readline())

    if comm != 0:
        heapq.heappush(heap, comm)
    else:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
        
