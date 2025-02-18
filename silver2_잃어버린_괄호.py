# https://www.acmicpc.net/problem/1541
import sys
INPUT = sys.stdin.readline
CALC = INPUT().strip()
List = []
num = ""
SUM = 0
method = "+"

for char in CALC:
    if char.isdigit():
        num += char
    else:
        List.append(int(num))
        List.append(char)
        num = ""
List.append(int(num))

for n in List:
    if n != '+' and n != '-' and method == '-':
        SUM -= n
        continue
    if n != '+' and n != '-':
        SUM += n
        continue
    if n == '-':
        method = '-'
        continue

print(SUM)