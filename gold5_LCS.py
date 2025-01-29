# 문제
# https://www.acmicpc.net/problem/9251
import sys
INPUT = sys.stdin.readline

strings = [list(INPUT().strip()) for _ in range(2)]
ilength = strings[0].__len__() + 1
alength = strings[1].__len__() + 1
dp = [[0] * max(alength,ilength) for _ in range(max(alength,ilength))]
for i in range(1, ilength):
    for a in range(1, alength):
        if strings[0][i-1] == strings[1][a-1]:
            dp[i][a] = dp[i-1][a-1] + 1
        else:
            dp[i][a] = max(dp[i-1][a], dp[i][a-1])

print(max(max(dp)))