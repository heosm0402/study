from collections import Counter

def solution(answers):

    p_1 = [1,2,3,4,5] * 2000
    p_2 = [2,1,2,3,2,4,2,5] * 1250
    p_3 = [3,3,1,1,2,2,4,4,5,5] * 1000

    for idx, answer in enumerate(answers):
        if answer == p_1[idx]:
            p_1[idx] = 0
        if answer == p_2[idx]:
            p_2[idx] = 0
        if answer == p_3[idx]:
            p_3[idx] = 0

    p_1 = Counter(p_1)
    p_2 = Counter(p_2)
    p_3 = Counter(p_3)

    count = [p_1.get(0, 0), p_2.get(0, 0), p_3.get(0, 0)]
    answer = [i for i, value in enumerate(count) if value == max(count)]
    
    return answer

solution([1,2,3,4,5])