# 문제
# https://www.acmicpc.net/problem/2565
import sys
INPUT = sys.stdin.readline

N = int(INPUT())
List = [[0] * N for _ in range(N)]
dp = [1] * N
for i in range(N):
    List[i] = list(map(int, INPUT().split()))

List.sort()

for i in range(1, N):
    for j in range(i):
        if List[j][1] < List[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))