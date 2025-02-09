# https://www.acmicpc.net/problem/2667
import sys, collections

INPUT = sys.stdin.readline
N = int(INPUT())

List = [[0] * (N + 2)] + [[0] + list(map(int, INPUT().strip())) + [0] for _ in range(N)] + [[0] * (N + 2)]
visited = [[0] * (N + 2) for _ in range(N + 2)]
deque = collections.deque
count = 0
results = []

for r in range(1, N + 1):
    for c in range(1, N + 1):
        if not visited[r][c] and List[r][c]:
            queue = deque([[r,c]])
            visited[r][c] = True
            # print(f'행 : {r} 열 : {c} 시작')
            while queue:
                node = queue.popleft()
                count += 1
                # print(f'node 꺼냄 {node}')
                if List[node[0] + 1][node[1]] and not visited[node[0] + 1][node[1]]:
                    queue.append([node[0] + 1, node[1]])
                    visited[node[0] + 1][node[1]] = True
                    # print(f'node 삽입 {[node[0] + 1, node[1]]}')
                if List[node[0] - 1][node[1]] and not visited[node[0] - 1][node[1]]:
                    queue.append([node[0] - 1, node[1]])
                    visited[node[0] - 1][node[1]] = True
                    # print(f'node 삽입 {[node[0] - 1, node[1]]}')
                if List[node[0]][node[1] + 1] and not visited[node[0]][node[1] + 1]:
                    queue.append([node[0], node[1] + 1])
                    visited[node[0]][node[1] + 1] = True
                    # print(f'node 삽입 {[node[0], node[1] + 1]}')
                if List[node[0]][node[1] - 1] and not visited[node[0]][node[1] - 1]:
                    queue.append([node[0], node[1] - 1])
                    visited[node[0]][node[1] - 1] = True
                    # print(f'node 삽입 {[node[0], node[1] - 1]}')

            results.append(count)
            count = 0

print(len(results))
for result in sorted(results):
    print(result)