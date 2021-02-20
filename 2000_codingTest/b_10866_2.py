from collections import deque

N = int(input())
dq = deque([])

for _ in range(N):
    comm = input().split()

    if comm[0] == 'push_front':
        dq.appendleft(comm[1])
    elif comm[0] =='push_back':
        dq.append(comm[1])
    elif comm[0] == 'pop_front':
        if len(dq):
            print(dq.popleft())
        else:
            print(-1)
    elif comm[0] == 'pop_back':
        if len(dq):
            print(dq.pop())
        else:
            print(-1)
    elif comm[0] == 'size':
        print(len(dq))
    elif comm[0] == 'empty':
        if len(dq):
            print(0)
        else:
            print(1)
    elif comm[0] == 'front':
        if len(dq):
            print(dq[0])
        else:
            print(-1)
    elif comm[0] == 'back':
        if len(dq):
            print(dq[-1])
        else:
            print(-1)