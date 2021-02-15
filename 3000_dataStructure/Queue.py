### 리스트로 Queue 구현하기

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


lq = ListQueue()
lq.enqueue(1)
lq.enqueue(2)
lq.enqueue(3)
lq.enqueue(4)
lq.enqueue(5)
lq.printQueue()

print(lq.dequeue())
print(lq.dequeue())
print(lq.dequeue())
print(lq.dequeue())
print(lq.dequeue())
lq.printQueue()