T = int(input())

for t in range(T):
    SUM = 0
    SUMList = []
    N, M = map(int, input().split())
    List = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1}',end=" ")
    for x in range(N-M+1):
        for y in range(N-M+1):

            for X in range(M):
                for Y in range(M):
                    SUM = SUM + List[x+X][y+Y]
            # print(SUM)
            SUMList.append(SUM)
            SUM=0


    print(max(SUMList))
