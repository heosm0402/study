N, K = map(int, input().split())

l = [n + 1 for n in range(N)]

s = []
cursor = 0

while len(l):
    cursor += K - 1 

    if len(l) <= cursor:
        cursor = (cursor % len(l))

    s.append(str(l.pop(cursor)))

print("<%s>" %(", ".join(s)))
