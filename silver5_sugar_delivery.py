# 문제
# https://www.acmicpc.net/problem/2839
# dp[T][F} T = 3킬로 봉지 개수, F = 5킬로 봉지 개수
import sys

INPUT = sys.stdin.readline

N = int(INPUT())

dp = [[0] * N for _ in range(N)]
sumList = []
F = 5
T = 3
Fnum = 0
Tnum = 5000
SUM = 5000
for f in range(N):
    if (F * f) >= N:
        break
    for t in range(N):
        dp[f][t] = (F * f) + (T * t)
        if dp[f][t] >= N:
            if dp[f][t] == N:
                sumList.append([t,f])
            break

for data in sumList:
    if SUM > sum(data):
        SUM = sum(data)

if(SUM == 5000):
    SUM = -1

print(SUM)


