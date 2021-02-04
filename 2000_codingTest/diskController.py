import heapq
import math
def solution(jobs):
    answer = 0
    time = 0

    h = []
    for i, j in jobs:
        heapq.heappush(h, (j, i))

    while h:
        low = heapq.heappop(h)
        answer += time + low[0] - low[1]
        time += low[0]
        print(f'time is {time} and answer is {answer}\n')
        
    print(int(math.floor(answer/len(jobs))))
    return int(math.floor(answer/len(jobs)))

solution([[0, 3], [1, 9], [2, 6]])

# 아직 못 풀음