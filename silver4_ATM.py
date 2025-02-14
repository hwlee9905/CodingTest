# https://www.acmicpc.net/problem/11399
import sys
INPUT = sys.stdin.readline
N = int(INPUT())
P = sorted(list(map(int, INPUT().split())))
dp = [0] * N
dp[0] = P[0]
for i in range(1, N):
    dp[i] = dp[i-1] + P[i]

print(sum(dp))