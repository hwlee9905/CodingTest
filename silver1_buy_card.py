import sys
INPUT = sys.stdin.readline

N = int(INPUT())
P = list(map(int, INPUT().split()))
P.insert(0,0)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + P[j])

print(dp[-1])