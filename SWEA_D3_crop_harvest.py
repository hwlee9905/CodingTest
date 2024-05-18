T = int(input())
for t in range(1, T+1):
    N = int(input())
    List = [list(map(int, input().strip())) for _ in range(N)]
    SUM = 0
    for y in range(N):
        if y < int(N/2):
            for x in range(int(N/2) - y, int(N/2) + y + 1):
                SUM = SUM + List[y][x]
        elif y == int(N/2):
            for x in range(N):
                SUM = SUM + List[y][x]
        else:
            for x in range(y - int(N/2), N - (y-int(N/2)) ):
                SUM = SUM + List[y][x]

    print(f'#{t} {SUM}')
