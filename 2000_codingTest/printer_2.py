def solution(priorities, location):
    answer = 0
    queue = []
    
    for i, p in enumerate(priorities):
        queue.append((i, p))

    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
        

solution([2, 1, 3, 2], 2)
print('\n')
solution([1, 1, 9, 1, 1, 1], 0)