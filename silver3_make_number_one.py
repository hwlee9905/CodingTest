# # 문제
# # https://www.acmicpc.net/problem/1463
#
# import sys
# INPUT = sys.stdin.readline
# N = int(INPUT())
# dp = [0] * (N + 1)
# count = 0
#
# for i in range(N, 0, -1):
#     if i == 1:
#         break
#
#     if dp[i - 1] != 0:
#         dp[i - 1] = min(dp[i] + 1, dp[i - 1])
#     else:
#         dp[i - 1] = dp[i] + 1
#
#     if i % 3 == 0:
#         if dp[int(i / 3)] != 0:
#             dp[int(i / 3)] = min(dp[int(i / 3)], dp[i] + 1)
#         else:
#             dp[int(i / 3)] = dp[i] + 1
#         # print(dp)
#         # print(i, "3으로 나눔")
#     if i % 2 == 0:
#         if dp[int(i / 2)] != 0:
#             dp[int(i / 2)] = min(dp[int(i / 2)], dp[i] + 1)
#         else:
#             dp[int(i / 2)] = dp[i] + 1
#         # print(dp)
#         # print(i, "2으로 나눔",dp[i], dp[int(i / 2)], int(i / 2))
#     # print(dp)
#
# print(dp[1])

import sys
INPUT = sys.stdin.readline
N = int(INPUT())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp)
