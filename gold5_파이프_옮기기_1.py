# https://www.acmicpc.net/problem/17070
import sys
INPUT = sys.stdin.readline
N = int(INPUT())

List = [list(map(int, INPUT().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

dp[0][0][1] = 1
for i in range(2, N):
    if List[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]