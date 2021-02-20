from collections import deque

cards = deque([n+1 for n in range(int(input()))])
cnt = 0

while len(cards) != 1:
    if cnt % 2 == 0:
        cards.popleft()
    else:
        cards.append(cards.popleft())

    cnt += 1

print(cards[0])