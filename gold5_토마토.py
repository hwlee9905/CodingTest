# https://www.acmicpc.net/problem/7576
import sys, collections
INPUT = sys.stdin.readline
M, N = map(int, INPUT().split())
List = [list(map(int, INPUT().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
deque = collections.deque
queue = deque([])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for r in range(N):
    for c in range(M):
        if List[r][c] == 1:
            queue.append([r,c])
            visited[r][c] = 1
        if List[r][c] == -1:
            visited[r][c] = 1

# print(queue)
while queue:
    node = queue.popleft()
    for v in range(4):
        nx, ny = dx[v] + node[1], dy[v] + node[0]
        if 0 <= ny < N and 0 <= nx < M:
            if List[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = visited[node[0]][node[1]] + 1
                queue.append([ny, nx])

# print(visited)
max_value = max(max(row) for row in visited)
min_value = min(min(row) for row in visited)
if min_value == 0:
    print(min_value - 1)
else:
    print(max_value - 1)
