T = int(input())
for t in range(1,T+1):
    deck = [[False]*14 for _ in range(4)]
    S = list(input().strip())
    SList = []
    for s in range(0,len(S),3):
        sList = [S[s], int(S[s+2]) + int(S[s+1])*10]
        SList.append(sList)
    # print(SList)

    for s in SList:
        if s[0] == 'S':
            if deck[0][s[1]]:
                deck[0][s[1]] = "ERROR"
            else:
                deck[0][s[1]] = True
        if s[0] == 'D':
            if deck[1][s[1]]:
                deck[1][s[1]] = "ERROR"
            else:
                deck[1][s[1]] = True
        if s[0] == 'H':
            if deck[2][s[1]]:
                deck[2][s[1]] = "ERROR"
            else:
                deck[2][s[1]] = True
        if s[0] == 'C':
            if deck[3][s[1]]:
                deck[3][s[1]] = "ERROR"
            else:
                deck[3][s[1]] = True

    print(f'#{t}', end=" ")
    countList = []
    ERROR = False
    for d in deck:
        if ERROR:
            break
        count = 13
        for c in d:
            if c:
                count = count - 1
            if c == 'ERROR':
                ERROR = True
                break
        countList.append(count)

    if ERROR:
        print('ERROR')
    else:
        for i in countList:
            print(i, end=" ")
        print()


