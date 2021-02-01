from queue import PriorityQueue

que_1 = PriorityQueue()

que_1.put(4)
que_1.put(1)
que_1.put(7)
que_1.put(3)

print(que_1.get())

que_2 = PriorityQueue()

que_2.put('Melon')
que_2.put('Banana')
que_2.put('Apple')

print(que_2.get())


que_3 = PriorityQueue()

que_3.put((3, 'Apple'))
que_3.put((4, 'Banana'))
que_3.put((1, 'Melon'))

print(que_3.get()[1])