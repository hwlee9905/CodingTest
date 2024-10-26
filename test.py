T = int(input())

for t in range(1,T+1):
    N = int(input())
    List = input().strip()
    count = 0
    visited = [False for _ in range(N)]
    for i in range(1,len(List)-1):
        visited[i] = True
        if List[i] == 'a' or List[i] == 'b':
            if (List[i-1] == 'a' and visited[i-1] == False) or (List[i-1] == 'b' and visited[i-1] == False):
                count = count + 1
                visited[i-1] = True
            if (List[i+1] == 'a' and visited[i+1] == False) or (List[i+1] == 'b' and visited[i+1] == False):
                count = count + 1
                visited[i+1] = True

    print(f'#{t} {count}')
