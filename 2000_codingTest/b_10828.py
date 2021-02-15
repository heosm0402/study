class ListQueue():
    def __init__(self):
        self.queue = []

    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(-1)

    def enqueue(self, n):
        self.queue.append(n)

    def printQueue(self):
        print(self.queue)

num_of_comm = int(input())

comm_list = []
for i in range(num_of_comm):
    comm_list.append(input())

lq = ListQueue()

for i in comm_list:
    temp_comm = i.split()
    if temp_comm[0] == 'push':
        lq.enqueue(temp_comm[1])
    elif temp_comm[0] == 'pop':
        if len(lq.queue) != 0:
            print(lq.dequeue())
        else:
            print(-1)
    elif temp_comm[0] == 'size':
        print(len(lq.queue))
    elif temp_comm[0] == 'empty':
        if len(lq.queue) == 0:
            print(1)
        else:
            print(0)
    elif temp_comm[0] == 'top':
        if len(lq.queue) != 0:
            print(lq.queue[-1])
        else:
            print(-1)
