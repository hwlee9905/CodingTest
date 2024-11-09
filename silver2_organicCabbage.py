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
    array = [[0] * (M) for _ in range(N)]
    visited = [[False] * (M) for _ in range(N)]

    for i in range(K):
        m, n = map(int, input().split())
        array[n][m] = 1

    for i in range(N):
        for j in range(M):
            if array[i][j] and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    dx = x - 1
                    if 0 <= dx < N and not visited[dx][y] and array[dx][y]:
                        queue.append((dx, y))
                        visited[dx][y] = True
                    dy = y - 1
                    if 0 <= dy < M and not visited[x][dy] and array[x][dy]:
                        queue.append((x, dy))
                        visited[x][dy] = True
                    dx = x + 1
                    if 0 <= dx < N and not visited[dx][y] and array[dx][y]:
                        queue.append((dx, y))
                        visited[dx][y] = True
                    dy = y + 1
                    if 0 <= dy < M and not visited[x][dy] and array[x][dy]:
                        queue.append((x, dy))
                        visited[x][dy] = True

                count += 1
    results.append(count)

for result in results:
    print(result)

# import collections
# import sys
# input = sys.stdin.readline
# deque = collections.deque
#
# T = int(input())
# results = []
#
# # 방향 벡터 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for _ in range(T):
#     count = 0
#     M, N, K = map(int, input().split())
#     array = [[0] * (M) for _ in range(N)]
#     visited = [[False] * (M) for _ in range(N)]
#
#     for i in range(K):
#         m, n = map(int, input().split())
#         array[n][m] = 1
#
#     for i in range(N):
#         for j in range(M):
#             if array[i][j] and not visited[i][j]:
#                 queue = deque([(i, j)])
#                 visited[i][j] = True
#                 while queue:
#                     x, y = queue.popleft()
#                     for d in range(4):
#                         nx, ny = x + dx[d], y + dy[d]
#                         if 0 <= nx < N and 0 <= ny < M and array[nx][ny] and not visited[nx][ny]:
#                             queue.append((nx, ny))
#                             visited[nx][ny] = True
#                 count += 1
#     results.append(count)
#
# for result in results:
#     print(result)

