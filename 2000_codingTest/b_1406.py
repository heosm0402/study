import sys


# if __name__ == "__main__":

N = sys.stdin.readline().strip()
M = int(sys.stdin.readline())
cur = len(N)

cnt = 0
# for _ in range(M):
#     comm = sys.stdin.readline().strip()
for line in sys.stdin:
    cnt += 1
    if line[0] == 'P':
        C, char = line.strip().split()
        N = N[0:cur-1] + char + N[cur:]
    else:
        if line[0] == 'L' and cur != 0:
            cur -= 1
        elif line[0] == 'D' and cur < len(N):
            cur += 1
        elif line[0] == 'B' and cur != 0 :
            N = N[0:cur-1] + N[cur:]

    if cnt == M:
        print(N)
        break