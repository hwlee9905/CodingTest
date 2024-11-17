# 문제
# https://www.acmicpc.net/problem/1010
import sys
input = sys.stdin.readline

def combination(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

T = int(input()) # Test CASE N
cases = []
case = 0

for _ in range(T):
    N, M = map(int, input().split())
    cases.append(combination(M, N))

for i in cases:
    print(i, end=" ")







