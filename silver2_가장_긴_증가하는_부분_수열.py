# https://www.acmicpc.net/problem/11053
import sys
INPUT = sys.stdin.readline
N = int(INPUT())
ai = list(map(int, INPUT().split()))
dp = [1] * N
maxList = []
for i in range(1, N):
    for back in range(i, -1, -1):
        if ai[i] > ai[back]:
            maxList.append(dp[back] + 1)

    if len(maxList) != 0:
        dp[i] = max(maxList)
        maxList =[]

    # if ai[i] > ai[i-1]:
    #     dp[i] = dp[i-1] + 1

    # print(dp)


# MAX = max([max(data) for data in dp])
# print(MAX)
print(max(dp))