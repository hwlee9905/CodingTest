# 문제
# https://www.acmicpc.net/problem/2156
# dp[W][N] N = 포도주, W = 포도주의 양
import sys
INPUT = sys.stdin.readline
N = int(INPUT())
WList = []
dp = [0 for _ in range(N)]
for _ in range(N):
    WList.append(int(INPUT()))

if N > 2:
    dp[2] = max(WList[0] + WList[2], WList[0] + WList[1], WList[1] + WList[2])
if N > 1:
    dp[1] = WList[0] + WList[1]
if N > 0:
    dp[0] = WList[0]


for i in range(3, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + WList[i] , dp[i - 3] + WList[i] + WList[i - 1])

print(dp[-1])


