# https://www.acmicpc.net/problem/11047
import sys
INPUT = sys.stdin.readline
N, K = map(int, INPUT().split())
coins = list(int(INPUT()) for _ in range(N))
count = 0

for i in range(N-1, -1, -1):
    if K // coins[i] != 0:
        count += K // coins[i]
        K %= coins[i]

print(count)