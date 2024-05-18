import collections
deque = collections.deque
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N+1)]
    maxLength = []

    Length = 1
    maxLength.append(Length)
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    stack = deque(graph[1])
    visited[1] = True
    while stack:
        # print(stack)
        lastNode = True
        current = stack.pop()
        Length = Length + 1
        visited[current] = True

        for i in graph[current]:
            if not visited[i]:
                stack.append(i)
                lastNode = False

        if lastNode:
            maxLength.append(Length)
            Length = 0



    print(f'#{t} {max(maxLength)}')





