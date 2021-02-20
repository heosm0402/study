K = int(input())

input_list = []
for _ in range(K):
    money = int(input())
    if money == 0:
        input_list.pop()
    else:
        input_list.append(money)

if len(input_list):
    print(sum(input_list))
else:
    print(0)