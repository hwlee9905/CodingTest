# 문제
# https://www.acmicpc.net/problem/1309
import sys
INPUT = sys.stdin.readline

N = int(INPUT())
dp = [0] * (N + 1)
dp[1] = 3
if N > 1:
    dp[2] = 7

for i in range(3, N + 1):
    dp[i] = (((dp[i-1] + dp[i-2]) * 2) - dp[i-2]) % 9901

print(dp[-1])