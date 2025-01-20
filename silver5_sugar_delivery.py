# 문제
# https://www.acmicpc.net/problem/2839
# dp[F][T} T = 3킬로 봉지 개수, F = 5킬로 봉지 개수
import sys, math
INPUT = sys.stdin.readline

N = int(INPUT())
tNum = math.floor(N/3) + 1
fNum = math.floor(N/5) + 1
dp = [[0] * tNum for _ in range(fNum)]
sumList = []

# print(tNum, fNum)
F = 5

T = 3
SUM = 5000
for f in range(fNum):
    if (F * f) > N:
        break
    for t in range(tNum):
        dp[f][t] = (F * f) + (T * t)
        if dp[f][t] >= N:
            if dp[f][t] == N:
                if (t + f) < SUM:
                    SUM = t + f
            break

if SUM == 5000:
    SUM = -1

# for data in dp:
#     print(data)

print(SUM)


