N, K = map(int, input().split())

coin_list = []
for i in range(N):
    coin_list.append(int(input()))

coin_list = sorted(coin_list, reverse=True)

coin_count = 0
for coin in coin_list:
    if K // coin != 0:
        coin_count += K // coin
        K -= coin * (K // coin)

print(coin_count)