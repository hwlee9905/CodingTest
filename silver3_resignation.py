# # 문제
# # https://www.acmicpc.net/problem/14501
# import sys
# INPUT = sys.stdin.readline
#
# N = int(INPUT())
# List = [list(map(int, INPUT().split())) for _ in range(N)]
# dp = [0] * (N + 1)
#
# for i in range(N):
#     if (i + List[i][0]) <= N:
#         # print(f'i + List[i][0]: {i + List[i][0]}')
#         dp[i] = max(dp[i - 1], dp[i])
#         dp[i + List[i][0]] = max(dp[i + List[i][0]], dp[i] + List[i][1])
#
# print(max(dp))

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n):
    print(f'i + arr[i][0] : {i + arr[i][0]}')
    for j in range(i + arr[i][0], n+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]
        print(dp)

print(dp[-1])