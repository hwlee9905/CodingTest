# 문제
# https://www.acmicpc.net/problem/9084

import sys
INPUT = sys.stdin.readline
T = int(INPUT())
NList = [0] * T
coinList = [[0] for _ in range(T)]
MList = [0] * T
results = [0] * T

for t in range(T):
    NList[t] = int(INPUT())
    coinList[t] = list(map(int, INPUT().split()))
    MList[t] = int(INPUT())

# for t in range(T):
#     start = MList[t] // coinList[t][-1]
#     for i in range(start, -1, -1):
#         temp = MList[t] - (i * coinList[t][-1])
#         for c in range(len(coinList[t]) - 2, -1, -1):
#             print(f'coinList[t][c] = {coinList[t][c]}, temp = {temp}')
#             if temp % coinList[t][c] == 0:
#                 results[t] += 1
#                 print(results[t])
#                 break
#             else:
#                 temp %= coinList[t][c]
#

for t in range(T):
    dp = [0] * (MList[t] + 1)
    dp[0] = 1
    for coin in coinList[t]:
        for i in range(1, MList[t] + 1):
            if coin <= i:
                dp[i] += dp[i-coin]
    print(dp[-1])