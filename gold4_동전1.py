# https://www.acmicpc.net/problem/2293
import sys
INPUT = sys.stdin.readline

n, k = map(int, INPUT().split())

coins = list(int(INPUT()) for _ in range(n))
dp = list(0 for _ in range(k + 1))
dp[0] = 1
for coin in coins:
    for i in range(1, k + 1):
        if coin <= i:
            dp[i] += dp[i - coin]

print(dp)