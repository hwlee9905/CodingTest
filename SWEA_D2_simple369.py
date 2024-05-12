N = int(input())
count = 0
for i in range(1,N+1):
    a = i
    while a :
        # print(f'i = {i}')
        # print(f'{i} % 10 = {i%10}')
        if (a%10 == 3) or (a%10 == 6) or (a%10 == 9):
            print("-",end="")
            count = count + 1
        a = int(a / 10)

    if count == 0:
        print(i, end=" ")
    else:
        print(" ",end="")

    count = 0