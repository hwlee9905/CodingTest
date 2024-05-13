T = int(input())
for t in range(T):
    N = int(input())
    List = [[] for _ in range(N)]
    print(f'#{t+1}')
    for index1, i in enumerate(range(N)):
        for index2, n in enumerate(range(i+1)):
            if (index2 == 0) or (index2 == i):
                List[i].append(1)
            else:
                List[i].append(List[i-1][n] + List[i-1][n-1])
    for i in List:
        for a in i:
            print(a, end=" ")
        print("")
