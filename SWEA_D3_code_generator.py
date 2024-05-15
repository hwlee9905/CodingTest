import collections
deque = collections.deque

for tc in range(1, 11):
    queue = deque()
    t = int(input())
    data = list(map(int, input().split()))
    popData = 1
    cycle = 5
    for i in data:
        queue.append(i)


    while popData != 0:
        if cycle == 5:
            cycle = 0

        cycle = cycle + 1
        popData = queue.popleft()
        popData = popData - cycle
        if popData <= 0:
            popData = 0

        queue.append(popData)

    print(f'#{tc}', end=" ")

    for i in queue:
        print(i,end=" ")

    print("")