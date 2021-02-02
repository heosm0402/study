import heapq

# 힙 생성 및 원소 추가
heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)
print('\n')

# heapify
heap2 = [50, 20, 10]
heapq.heapify(heap2)

print(heap2)
print('\n')

# 원소 삭제 및 인덱싱
result = heapq.heappop(heap)
print(result, heap)

result2 = heap[0]
print(result2, heap)
print('\n')

# max heap 만들기
heap_item = [1, 3, 5, 7, 9]

max_heap = []
for item in heap_item:
    heapq.heappush(max_heap, (-item, item))

max_item = heapq.heappop(max_heap)[1]
print(max_item)