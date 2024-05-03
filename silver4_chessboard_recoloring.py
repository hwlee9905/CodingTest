from sys import stdin
input = stdin.readline

B_arr = [['B','W','B',"W","B",'W',"B",'W'],
         ['W','B',"W","B",'W',"B",'W','B'],
         ['B','W','B',"W","B",'W',"B",'W'],
         ['W','B',"W","B",'W',"B",'W','B'],
         ['B','W','B',"W","B",'W',"B",'W'],
         ['W','B',"W","B",'W',"B",'W','B'],
         ['B','W','B',"W","B",'W',"B",'W'],
         ['W','B',"W","B",'W',"B",'W','B']]
W_arr = [['W','B',"W","B",'W',"B",'W','B'],
         ['B','W','B',"W","B",'W',"B",'W'],
         ['W','B',"W","B",'W',"B",'W','B'],
         ['B','W','B',"W","B",'W',"B",'W'],
         ['W','B',"W","B",'W',"B",'W','B'],
         ['B','W','B',"W","B",'W',"B",'W'],
         ['W','B',"W","B",'W',"B",'W','B'],
         ['B','W','B',"W","B",'W',"B",'W']]

a, b = map(int, input().split())
arr = [list(input().strip()) for _ in range(a)]
count = 0
count2 = 0
result = 1000000
# K, J 부터 시작하는 8x8 배열 추출
for k in range(a-7):
    for j in range(b-7):
        sub_arr = [arr[i][j:j+8] for i in range(k, k+8)]
        for i, row in enumerate(sub_arr):
            for j, value in enumerate(row):
                if(value != W_arr[i][j]):
                    count = count + 1
                if(value != B_arr[i][j]):
                    count2 = count2 + 1
                # print(value, end=" ")
        # print(f'count = {count} count2 = {count2}')
        if(count >= count2):
            if(result > count2):
                result = count2
        else:
            if(result > count):
                result = count
        count = 0
        count2 = 0
print(result)