for tc in range(1,11):
    N = int(input())
    List = list(map(int, input().split()))
    SUM = 0
    for i in range(2, len(List)-2):
        light = []
        light.append(List[i] - List[i-2])
        light.append(List[i] - List[i-1])
        light.append(List[i] - List[i + 1])
        light.append(List[i] - List[i + 2])
        if min(light) > 0:
            SUM = SUM + min(light)

    print(f'#{tc} {SUM}')