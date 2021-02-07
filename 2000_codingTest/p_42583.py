import time

def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_weight = 0
    on_list = {}

    while on_list or truck_weights:
        print(answer, on_list, truck_weights, on_weight)
        len_truck = len(truck_weights)
        answer += 1

        del_key_list = []
        for k in on_list:
            if answer - on_list.get(k)[0] == bridge_length:
                on_weight -= on_list.get(k)[1]
                del_key_list.append(k)

        for k in del_key_list:
            on_list.pop(k)

        if truck_weights and on_weight + truck_weights[0] <= weight:
            on_weight += truck_weights[0]
            on_list[len_truck] = [answer, truck_weights[0]]
            truck_weights.pop(0)

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

solution(bridge_length, weight, truck_weights)

# bridge_length = 100
# weight = 100
# truck_weights = [10]

# solution(bridge_length, weight, truck_weights)