#BOJ 2089 -2진수
import sys

N = int(sys.stdin.readline())
li = []
if N == 0:
    li.append(0)
else:
    while True:
        if N < 0:
            if N % 2 == 1:
                li.append(1)
                N = abs(N) // 2 + 1
            else:
                li.append(0)
                N = abs(N) // 2
        elif N > 0:
            if N % 2 == 1:
                li.append(1)
            else:
                li.append(0)
            N = -(N // 2)
        elif N == 0:
            break

for i in range(len(li)-1, -1, -1):
    print(li[i], end='')