# 문제
# https://www.acmicpc.net/problem/2583
import sys

input = sys.stdin.readline
M, N, K = map(int, input().split())
array = [[False] * (N+1) for _ in range(M+1)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            array[x][y] = True
    