import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) >= 2:
        low_1 = heapq.heappop(scoville)

        if low_1 <= K:
            low_2 = heapq.heappop(scoville)
            temp = low_1 + (low_2 * 2)
            answer += 1
            heapq.heappush(scoville, temp)
        else:
            print(answer)
            return answer

    if scoville[0] >= K:
        return answer
    else:
        return -1


solution([1, 2, 3, 9, 10, 12], 7)