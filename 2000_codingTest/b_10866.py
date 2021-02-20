class Deque():
    def __init__(self):
        self.deque = []

    def push_front(self, k):
        self.deque.insert(0, k)

    def push_back(self, k):
        self.deque.append(k)

    def pop_front(self):
        if len(self.deque):
            print(self.deque.pop(0))
        else:
            print(-1)

    def pop_back(self):
        if len(self.deque):
            print(self.deque.pop())
        else:
            print(-1)
    
    def size(self):
        print(len(self.deque))

    def empty(self):
        if len(self.deque):
            print(0)
        else:
            print(1)

    def front(self):
        if len(self.deque):
            print(self.deque[0])
        else:
            print(-1)

    def back(self):
        if len(self.deque):
            print(self.deque[-1])
        else:
            print(-1)

N = int(input())

dq = Deque()

for _ in range(N):
    command = input().split()
    if len(command) == 2:
        comm = command[0]
        K = command[1]
    else:
        comm = command[0]

    if comm == 'push_front':
        dq.push_front(K)
    elif comm == 'push_back':
        dq.push_back(K)
    elif comm == 'pop_front':
        dq.pop_front()
    elif comm == 'pop_back':
        dq.pop_back()
    elif comm == 'size':
        dq.size()
    elif comm == 'empty':
        dq.empty()
    elif comm == 'front':
        dq.front()
    elif comm == 'back':
        dq.back()