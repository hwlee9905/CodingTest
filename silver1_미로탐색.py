# # https://www.acmicpc.net/problem/2178
# import sys, collections
# INPUT = sys.stdin.readline
# N, M = map(int, INPUT().split())
# List = [[0] * (M + 2)] + [[0] + list(map(int, INPUT().strip()))  + [0] for _ in range(N)] + [[0] * (M + 2)]
# visited = [[0] * (M + 2) for _ in range(N + 2)]
# deque = collections.deque
# queue = deque([[1,1,1]])
# visited[1][1] = True
# MIN = 0
# while queue:
#     node = queue.popleft()
#     if node[0] == N and node[1] == M:
#         if MIN == 0:
#             MIN = node[2]
#         elif MIN > node[2]:
#             MIN = node[2]
#
#     dy = node[0] + 1
#     mdy = node[0] - 1
#     dx = node[1] + 1
#     mdx = node[1] - 1
#     if List[dy][node[1]] and not visited[dy][node[1]]:
#         queue.append([dy, node[1], node[2] + 1])
#         if not (dy == N and node[1] == M):
#             visited[dy][node[1]] = True
#     if List[node[0]][dx] and not visited[node[0]][dx]:
#         queue.append([node[0], dx, node[2] + 1])
#         if not (node[0] == N and dx == M):
#             visited[node[0]][dx] = True
#     if List[mdy][node[1]] and not visited[mdy][node[1]]:
#         queue.append([mdy, node[1], node[2] + 1])
#         if not (mdy == N and node[1] == M):
#             visited[mdy][node[1]] = True
#     if List[node[0]][mdx] and not visited[node[0]][mdx]:
#         queue.append([node[0], mdx, node[2] + 1])
#         if not (node[0] == N and mdx == M):
#             visited[node[0]][mdx] = True
#
# print(MIN)

# 풀이  ㅍ 
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 2차원 리스트 생성
graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

queue = deque([(0, 0)])

# 미로 문제 풀 때는 이동을 표현해준다.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

# BFS
while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:  # 범위 확인
            if graph[next_x][next_y] == 1:  # 경로 확인
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1  # value 자체를 이동 횟수로 사용

print(graph[N-1][M-1])