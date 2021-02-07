def solution(numbers):
    answer = []
    
    for idx, number_1 in enumerate(numbers):
        for number_2 in numbers[idx+1:]:
            if number_1 + number_2 not in answer:
                answer.append(number_1 + number_2)
    
    return sorted(answer)