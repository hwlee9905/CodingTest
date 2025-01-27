# 문제
# https://www.acmicpc.net/problem/11057
import sys
INPUT = sys.stdin.readline
N = int(INPUT())
num = 10
dp = [0] * (N + 1)
dp[1] = num

for i in range(2, N + 1):
    dp[i] = (dp[i - 1] * (num + (i - 1))) // i

print(dp[-1] % 10007)