import sys, collections
deque = collections.deque
input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start):
    visitSequence = []
    queue = deque([start])
    visited = [False for _ in range(N+1)]
    visited[start] = True

    while queue:
        node = queue.popleft()
        visitSequence.append(node)
        for i in sorted(graph[node]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    return visitSequence

def dfs(graph, start):
    visitSequence = []
    stack = [start]
    visited = [False for _ in range(N+1)]
    visited[start] = True

    while stack:
        node = stack.pop()
        visitSequence.append(node)

        for i in reversed(sorted(graph[node])):
            if not visited[i]:
                visited[i] = True
                stack.append(i)

    return visitSequence



for n in dfs(graph, V):
    print(n, end=" ")

print()

for n in bfs(graph, V):
    print(n, end=" ")
