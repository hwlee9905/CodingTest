# 문제
# https://www.acmicpc.net/problem/2606

# 예제 입력 1
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# 예제 출력 1
# 4

import sys, collections
deque = collections.deque
input = sys.stdin.readline

# N: 컴퓨터의 수, M: 연결되어 있는 컴퓨터 쌍의 수
N = int(input())
M = int(input())

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(N+1)]

# 간선 정보를 입력받아 그래프에 추가
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, start):
    visitSequence = []
    stack = deque([start])
    visited = [False for _ in range(N+1)]
    visited[start] = True

    while stack:
        node = stack.pop()
        visitSequence.append(node)

        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

    return visitSequence

print(len(dfs(graph, 1)) - 1)

# import collections
# import sys
# input = sys.stdin.readline
# deque = collections.deque
#
# T = int(input())
# results = []
#
# for _ in range(T):
#     count = 0
#     M, N, K = map(int, input().split())
#     array = [[0] * M for _ in range(N)]
#     visited = [[False] * M for _ in range(N)]
#
#     for _ in range(K):
#         m, n = map(int, input().split())
#         array[n][m] = 1
#
#     def bfs(x, y):
#         queue = deque([(x, y)])
#         visited[x][y] = True
#         while queue:
#             x, y = queue.popleft()
#             for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < N and 0 <= ny < M and array[nx][ny] and not visited[nx][ny]:
#                     queue.append((nx, ny))
#                     visited[nx][ny] = True
#
#     for i in range(N):
#         for j in range(M):
#             if array[i][j] and not visited[i][j]:
#                 bfs(i, j)
#                 count += 1
#
#     results.append(count)
#
# for result in results:
#     print(result)