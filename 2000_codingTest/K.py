def solution(array, commands):
    answer = []

    for i, j, k in commands:
        # print(i, j, k)

        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])