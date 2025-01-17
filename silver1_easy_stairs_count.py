# 문제
# https://www.acmicpc.net/problem/10844
# 0으로 시작하는 수는 계단수가 아님..
# dp[i][j] : i자리 수인 계단 수 중에 맨 끝이 j인 수의 개수
import sys
input = sys.stdin.readline

N = int(input())
dp = [10 * [0] for _ in range(0,N + 1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2,N + 1):
    for j in range (10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            
sum = 0
for i in dp[N]:
    sum += i

print(sum % 1000000000)

