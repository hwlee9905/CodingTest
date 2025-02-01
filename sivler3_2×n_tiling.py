# 문제
# https://www.acmicpc.net/problem/11726
import sys
INPUT = sys.stdin.readline

N = int(INPUT())
dp = [0] * (N + 1)

if N > 0:
    dp[1] = 1
if N > 1:
    dp[2] = 2
for i in range(3, N + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[-1] % 10007)