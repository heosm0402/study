def solution(priorities, location):
    answer = 0
    test = True
    

    while test:
        print(priorities, location)
        target = priorities.pop(0)
        big_test = True

        if location == 0:
            print("--")
            for i in priorities:
                if target < i:
                    big_test = False
                else:
                    pass
            
            if big_test:
                answer += 1
                return answer
                location -= 1
                test = False
            else:
                priorities.append(target)
                location = len(priorities) - 1
        else:
            print("==")
            for i in priorities:
                print(target, i)
                if target < i:
                    big_test = False
                else:
                    pass

            if big_test:
                answer += 1
                location -= 1
            else:
                location -= 1
                priorities.append(target)