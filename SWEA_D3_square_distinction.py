
T = int(input())

for t in range(1, T+1):
    squareXLen = 0
    squareYLen = []
    startSquare = False
    N = int(input())
    array = [list(input().strip()) for _ in range(N)]
    for row in array:
        squareXLen = 0
        startSquare = False
        for column in row:
            if column == '#':
                squareXLen = squareXLen + 1
                startSquare = True

            if column == '.' and startSquare == True:
                # print(f'squareLen = {squareXLen}')
                break

        if squareXLen > 0:
            squareYLen.append(squareXLen)



    count = 0
    print(f'#{t}', end=" ")
    for x in squareYLen:
        # print(f'x==squreXLen {x} {squareXLen}')
        if x == len(squareYLen):
            # print(f'count = {count}')
            count = count + 1
        else:
            print("no")
            break

    if count == len(squareYLen):
        print("yes")





    # print(squareYLen)