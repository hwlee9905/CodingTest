# https://www.acmicpc.net/problem/5585
import sys
INPUT = sys.stdin.readline
N = int(INPUT())
coins = [500, 100, 50, 10, 5, 1]
rest = 1000 - N
SUM = 0
for coin in coins:
    if rest >= coin:
        SUM += rest // coin
        rest -= coin * (rest // coin)
        # print(rest)

print(SUM)
