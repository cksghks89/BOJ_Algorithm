#BOJ 1978 소수 찾기
import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

num = 0
for i in li:
    temp = 0
    for j in range(2, i+1):
        if i % j == 0:
            temp += 1
    if temp == 1:
        num += 1

print(num)