TC = int(input())
# originList = [[] for _ in range(TC)]
for tc in range(TC):
    originList = []
    N = int(input())
    List = []
    List = list(map(int,input().split()))
    while List:
        for i in List:
            # print(f'current = {List[i]}')
            if (i in List) and (int(i * 0.75) in List):
                # print(i * 0.75 in List)
                # print(f'currnet = {current}, o = {o}, List = {List}')
                originList.append(int(i * 0.75))
                List.remove(i)
                List.remove(int(i*0.75))
                break
    print(f'#{tc + 1}', end=" ")
    for i in originList:
        print(i, end=" ")
    print("")

