T = int(input())
def dp(i, sum):
    global count
    if i == N:
        if sum == K:
            count = count + 1
        return

    # print(count)
    dp(i + 1, sum + A[i])
    dp(i + 1, sum)

for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    dp(0, 0)
    print(f'#{t+1}',end=" ")
    print(count)

