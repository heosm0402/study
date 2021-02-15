N = int(input())

time_list = sorted(map(int, input().split()))

time_spend = 0

for idx, time in enumerate(time_list):
    time_spend += time * (len(time_list) - idx)

print(time_spend)