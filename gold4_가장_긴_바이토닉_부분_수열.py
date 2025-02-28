# https://www.acmicpc.net/problem/11054
import sys
INPUT = sys.stdin.readline
N = int(INPUT())
arr = list(map(int, INPUT().split()))
dp = [1] * N
dp2 = [1] * N
current = 0
maxList = []

for i in range(1, N):
    for back in range(i):
        if arr[i] > arr[back]:
            maxList.append(dp[back] + 1)

    if len(maxList) != 0:
        dp[i] = max(maxList)
        maxList =[]

for i in range(N, -1, -1):
    for back in range(i, N):
        if arr[i] > arr[back]:
            maxList.append(dp2[back] + 1)

    if len(maxList) != 0:
        dp2[i] = max(maxList)
        maxList =[]

for i in range(N):
    dp2[i] += dp[i] - 1

print(max(dp2))