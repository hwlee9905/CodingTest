# 문제
# https://www.acmicpc.net/problem/10810
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list = [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i - 1, j):
        list[n] = k

for i in list:
    print(i, end=" ")