#BOJ 11653 소인수분해
import sys

N = int(sys.stdin.readline())

temp = 2
while True:
    if N == 1:
        break
    elif N % temp != 0:
        temp += 1
    else:
        print(temp)
        N = N//temp