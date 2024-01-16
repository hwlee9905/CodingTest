# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
import sys
data = sys.stdin.readline().rstrip().lower()
charlist=[]
freq=""
count=0
countfreq=0
# 초기 빈 2차원 리스트 생성

def findchar(char):
    # print(f'in findchar {char}')
    i=0
    for c in charlist:
        if c[0] == char:
            # print(f'c = {c[0]} char = {char} i = {i}')
            return i
        i += 1
        
    return char
for char in data:
    charlistcolumn = []
    findrs = findchar(char)
    if  findrs == char:
        charlistcolumn.append(char)
        charlistcolumn.append(1)
        charlist.append(charlistcolumn)
    else:
         charlist[findrs][1] += 1

for num in charlist:
    if num[1] > count:
        count = num[1]
        freq = num[0]
for num in charlist:
    if num[1] == count:
        countfreq += 1
if countfreq > 1:
    print("?")
else:
    print(freq.upper())
    
