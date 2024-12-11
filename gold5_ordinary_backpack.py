# 문제
# https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 물품의 수, 무게
dp = [[0] * (N + 1) for _ in range(K + 1)]
WList = [[0] for _ in range(N + 1)]
VList = [[0] for _ in range(N + 1)]
for i in range(1, N + 1):
    WList[i], VList[i] = map(int, input().split()) # 무게, 가치

for k in range(1, K + 1): # 최대 무게 k
    for n in range(1, N + 1): # 물품 n
        if k >= WList[n]:
            dp[k][n] = max(dp[k - WList[n]][n - 1] + VList[n], dp[k][n - 1])
        else:
            dp[k][n] = dp[k][n - 1]

print(dp[-1][-1])