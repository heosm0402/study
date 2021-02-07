def solution(board, moves):
    answer = 0
    box = []
    
    for m in moves:
        for row in board:
            if row[m-1] == 0:
                pass
            else:
                box.append(row[m-1])
                row[m-1] = 0
                break
        
        test = True
        
        while test:
            if len(box) >= 2 and box[-1] == box[-2]:
                answer += 2
                box.pop(-1)
                box.pop(-1)
            else:
                test = False
        
    return answer