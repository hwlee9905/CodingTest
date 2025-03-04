# https://www.acmicpc.net/problem/5430
import sys, collections
INPUT = sys.stdin.readline
T = int(INPUT())

for _ in range(T):
    reverse = False # True = 뒤집은 상태, False = 원래의 상태
    error = False
    p = list(INPUT().strip())
    n = int(INPUT())
    try:
        x = list(map(int, INPUT().strip().strip('[]').split(',')))
        for calc in p:
            if calc == 'R':
                if reverse:
                    reverse = False
                else:
                    reverse = True
            elif calc == 'D':
                if len(x) == 0:
                    print('error')
                    error = True
                    break
                elif reverse:
                    x.pop()
                else:
                    x.pop(0)

        if error:
            continue
        else:
            print('[', end='')
            if reverse:
                for i in range(len(x) - 1, -1, -1):
                    if i == 0:
                        print(x[i], end='')
                    else:
                        print(x[i], end=',')
            else:
                for i in range(len(x)):
                    if i + 1 == len(x):
                        print(x[i], end='')
                    else:
                        print(x[i], end=',')
            print(']')
    except Exception:

        for calc in p:
            if calc == 'D':
                print('error')
                error = True
                break
        if error:
            continue
        else:
            print('[]')



