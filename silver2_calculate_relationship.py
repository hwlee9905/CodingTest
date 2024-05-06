from collections import deque
from sys import stdin
input = stdin.readline

person_count = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(person_count+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start_node, end_node):
    visited = [-1 for _ in range(person_count+1)]
    queue = deque([start_node])
    visited[start_node] = 0
    while queue:
        node = queue.popleft()
        print(graph[node])
        for i in graph[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + 1
                queue.append(i)
    print(visited)
    return visited[end_node]

print(bfs(graph, a, b))
