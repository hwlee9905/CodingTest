import sys, collections

from SWEA_D3_code_generator import queue

deque = collections.deque
input = sys.stdin.readline

# N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점 번호
N, M, V = map(int, input().split())

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(N+1)]

# 간선 정보를 입력받아 그래프에 추가
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# BFS (너비 우선 탐색) 함수 정의
def bfs(graph, start):
    visitSequence = []  # 방문 순서를 저장할 리스트
    queue = deque([start])  # 시작 정점을 큐에 추가
    visited = [False for _ in range(N+1)]  # 방문 여부를 저장할 리스트
    visited[start] = True  # 시작 정점을 방문 처리

    while queue:
        node = queue.popleft()  # 큐에서 정점을 꺼냄
        visitSequence.append(node)  # 방문 순서에 추가
        for i in sorted(graph[node]):  # 현재 정점과 연결된 정점들을 정렬하여 순회
            if not visited[i]:  # 방문하지 않은 정점이라면
                visited[i] = True  # 방문 처리
                queue.append(i)  # 큐에 추가

    return visitSequence  # 방문 순서를 반환

# DFS (깊이 우선 탐색) 함수 정의
def dfs(graph, start):
    visitSequence = []  # 방문 순서를 저장할 리스트
    stack = [start]  # 시작 정점을 스택에 추가
    visited = [False for _ in range(N+1)]  # 방문 여부를 저장할 리스트
    visited[start] = True  # 시작 정점을 방문 처리

    while stack:
        node = stack.pop()  # 스택에서 정점을 꺼냄
        visitSequence.append(node)  # 방문 순서에 추가

        for i in reversed(sorted(graph[node])):  # 현재 정점과 연결된 정점들을 정렬하여 역순으로 순회
            if not visited[i]:  # 방문하지 않은 정점이라면
                visited[i] = True  # 방문 처리
                stack.append(i)  # 스택에 추가

    return visitSequence  # 방문 순서를 반환

# DFS 결과 출력
for n in dfs(graph, V):
    print(n, end=" ")

print()

# BFS 결과 출력
for n in bfs(graph, V):
    print(n, end=" ")