import sys
INPUT = sys.stdin.readline

N = int(INPUT())
P = list(map(int, INPUT().split()))
P.insert(0,0)
dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    if N % i:
        dp[i] = int((P[i] * (N // i)) + P[(N % i)])
    else:
        dp[i] = int(P[i] * (N / i))

print(max(dp))