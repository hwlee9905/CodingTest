import collections
deque = collections.deque
T = int(input())
def dfs(x, y, stack):
    global isGomoku
    # print(f'stack = {stack}')
    if isGomoku:
        return
    if len(stack) == 5:
        isGomoku = True
        return
    if x == N or y == N:
        return

    if Board[x][y] == 'o':
        stack.append(Board[x][y])
    else:
        stack.clear()

    dfs(x+1, y, stack.copy())
    dfs(x, y+1, stack.copy())
    dfs(x+1, y+1, stack.copy())

def dfs2(y, x, stack):
    global isGomoku
    if isGomoku:
        return
    if len(stack) == 5:
        isGomoku = True
        return
    if x < 0 or y == N:
        return
    # print(f'x, y = {x}, {y}')
    # print(f'Board[x][y] = {Board[y][x]}')
    if Board[y][x] == 'o':
        stack.append(Board[y][x])

    else:
        stack.clear()

    dfs2(y+1, x-1, stack.copy())

for t in range(1, T+1):
    N = int(input())
    Board = [list(input().strip()) for _ in range(N)]
    isGomoku = False
    init = deque(Board[0][0])
    dfs(0,0,init)
    init2 = deque(Board[0][N-1])
    dfs2(0, N-1,init2)
    if isGomoku:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")