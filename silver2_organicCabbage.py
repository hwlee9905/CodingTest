# 문제
# https://www.acmicpc.net/problem/1012
import collections
import sys
input = sys.stdin.readline
deque = collections.deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    List = [[] for _ in range(K)]
    array = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for i in range(K):
        m, n = map(int, input().split())
        array[n][m] = 1

    queue = deque([])

    for i, row in enumerate(visited):
        for j, column in enumerate(row):
            visited[i][j] = True
            if column:
                queue.



    print()
    for row in array:
        print(row)





