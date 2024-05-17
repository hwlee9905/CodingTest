T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    Board = [[0]*(N+2) for _ in range(N+2)]
    MList = [list(map(int, input().split())) for _ in range(M)]

    #init
    Board[int(N / 2)][int(N / 2)] = 2
    Board[int(N / 2)][int(N / 2) + 1] = 1
    Board[int(N / 2) + 1][int(N / 2)] = 1
    Board[int(N / 2) + 1][int(N / 2) + 1] = 2
    print(Board)

    for mList in MList:

        #흑돌이 놓았을때
        if mList[2] == 1:
            #놓은위치
            Board[mList[1]][mList[0]] = 1
            while (
                #오른쪽 확인
                (Board[mList[1]][mList[0] + 1] == 2) or
                #오른쪽 아래 확인
                (Board[mList[1] - 1][mList[0] + 1] == 2) or
                #아래 확인
                (Board[mList[1] - 1][mList[0]] == 2) or
                #왼쪽 아래 확인
                (Board[mList[1] - 1][mList[0] - 1] == 2) or
                #왼쪽 확인
                (Board[mList[1]][mList[0] - 1] == 2) or
                #왼쪽 위 확인
                (Board[mList[1] + 1][mList[0] - 1] == 2) or
                #위 확인
                (Board[mList[1] + 1][mList[0]] == 2) or
                #오른쪽 위 확인
                (Board[mList[1] + 1][mList[0] + 1] == 2)
            ) :
                print(f'흑돌 놓는 차례 mList = {mList}')
                if Board[mList[1]][mList[0] + 1] == 2:
                    Board[mList[1]][mList[0] + 1] = 1

                if Board[mList[1] - 1][mList[0] + 1] == 2:
                    Board[mList[1] - 1][mList[0] + 1] = 1

                if Board[mList[1] - 1][mList[0]] == 2:
                    Board[mList[1] - 1][mList[0]] = 1

                if Board[mList[1] - 1][mList[0] - 1] == 2:
                    Board[mList[1] - 1][mList[0] - 1] = 1

                if Board[mList[1]][mList[0] - 1] == 2:
                    Board[mList[1]][mList[0] - 1] = 1

                if Board[mList[1] + 1][mList[0] - 1] == 2:
                    Board[mList[1] + 1][mList[0] - 1] = 1

                if Board[mList[1] + 1][mList[0]] == 2:
                    Board[mList[1] + 1][mList[0]] = 1

                if Board[mList[1] + 1][mList[0] + 1] == 2:
                    Board[mList[1] + 1][mList[0] + 1] = 1

        #백돌이 놓았을때
        if mList[2] == 2:
            #놓은위치
            Board[mList[1]][mList[0]] = 2
            while (
                    # 오른쪽 확인
                    (Board[mList[1]][mList[0] + 1] == 1) or
                    # 오른쪽 아래 확인
                    (Board[mList[1] - 1][mList[0] + 1] == 1) or
                    # 아래 확인
                    (Board[mList[1] - 1][mList[0]] == 1) or
                    # 왼쪽 아래 확인
                    (Board[mList[1] - 1][mList[0] - 1] == 1) or
                    # 왼쪽 확인
                    (Board[mList[1]][mList[0] - 1] == 1) or
                    # 왼쪽 위 확인
                    (Board[mList[1] + 1][mList[0] - 1] == 1) or
                    # 위 확인
                    (Board[mList[1] + 1][mList[0]] == 1) or
                    # 오른쪽 위 확인
                    (Board[mList[1] + 1][mList[0] + 1] == 1)
            ):
                print(f'백돌 놓는 차례 mList = {mList}')
                if Board[mList[1]][mList[0] + 1] == 1:
                    Board[mList[1]][mList[0] + 1] = 2

                if Board[mList[1] - 1][mList[0] + 1] == 1:
                    Board[mList[1] - 1][mList[0] + 1] = 2

                if Board[mList[1] - 1][mList[0]] == 1:
                    Board[mList[1] - 1][mList[0]] = 2

                if Board[mList[1] - 1][mList[0] - 1] == 1:
                    Board[mList[1] - 1][mList[0] - 1] = 2

                if Board[mList[1]][mList[0] - 1] == 1:
                    Board[mList[1]][mList[0] - 1] = 2

                if Board[mList[1] + 1][mList[0] - 1] == 1:
                    Board[mList[1] + 1][mList[0] - 1] = 2

                if Board[mList[1] + 1][mList[0]] == 1:
                    Board[mList[1] + 1][mList[0]] = 2

                if Board[mList[1] + 1][mList[0] + 1] == 1:
                    Board[mList[1] + 1][mList[0] + 1] = 2

    print(Board)