# class ListQueue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, n):
#         self.queue.append(n)

#     def dequeue(self):
#         if len(self.queue) == 0:
#             return -1
#         return self.queue.pop(0)
    
#     def front_deque(self):
#         if len(self.queue) == 0:
#             return -1
#         return self.queue[0]

#     def back_deque(self):
#         if len(self.queue) == 0:
#             return -1
#         return self.queue[-1]

#     def size(self):
#         return len(self.queue)

#     def empty(self):
#         if len(self.queue) == 0:
#             return 1
#         else:
#             return 0

# lq = ListQueue()

num_comm = int(input())

# for i in range(num_comm):
#     temp = input().split()
#     if temp[0] == 'push':
#         lq.enqueue(temp[1])
#     elif temp[0] == 'front':
#         print(lq.front_deque())
#     elif temp[0] == 'back':
#         print(lq.back_deque())
#     elif temp[0] == 'size':
#         print(lq.size())
#     elif temp[0] == 'empty':
#         print(lq.empty())
#     elif temp[0] == 'pop':
#         print(lq.dequeue())

lq = []

comm_list = []

for _ in range(num_comm):
    comm_list.append(input().split())

for temp in comm_list:
    if temp[0] == 'push':
        lq.append(temp[1])
    elif temp[0] == 'front':
        if len(lq) == 0:
            print(-1)
        else:
            print(lq[0])
    elif temp[0] == 'back':
        if len(lq) == 0:
            print(-1)
        else:
            print(lq[-1])
    elif temp[0] == 'size':
        print(len(lq))
    elif temp[0] == 'empty':
        if len(lq) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == 'pop':
        if len(lq) == 0:
            print(-1)
        else:
            print(lq.pop(0))