#BOJ 1168 조세퍼스 문제2
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

li = [0 for i in range(0, N)]
for i in range(0, N):
    li[i] = i+1

index = K-1
printlist = []
while len(li) != 0:
    index = index % len(li)
    printlist.append(li.pop(index))
    index += K-1

print("<"+", ".join(map(str, printlist[:len(printlist)]))+">", end='')

