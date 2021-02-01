from collections import deque

dq = deque([])

dq.append(1)
dq.append(2)
dq.append(3)
print(dq.appendleft(4))
print(dq)

print(dq.popleft())
print(dq.popleft())
print(dq)
print(dq.pop())
print(dq.popleft())
print(dq)