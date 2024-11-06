# 문제
# https://www.acmicpc.net/problem/1012
import collections
import sys
input = sys.stdin.readline
deque = collections.deque

T = int(input())
results = []

for _ in range(T):
    count = 0
    M, N, K = map(int, input().split())
    array = [[0] * (M + 2) for _ in range(N + 2)]
    visited = [[False] * (M + 2) for _ in range(N + 2)]

    for i in range(K):
        m, n = map(int, input().split())
        array[n][m] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if array[i][j] and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    if array[x][y + 1] and not visited[x][y + 1]:
                        queue.append((x, y + 1))
                        visited[x][y + 1] = True
                    if array[x][y - 1] and not visited[x][y - 1]:
                        queue.append((x, y - 1))
                        visited[x][y - 1] = True
                    if array[x + 1][y] and not visited[x + 1][y]:
                        queue.append((x + 1, y))
                        visited[x + 1][y] = True
                    if array[x - 1][y] and not visited[x - 1][y]:
                        queue.append((x - 1, y))
                        visited[x - 1][y] = True
                count += 1
    results.append(count)

for result in results:
    print(result)



