#BOJ 11576 Base Conversion
import sys

A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
ABase = list(map(int, sys.stdin.readline().split()))

tenBase = 0
baseindex = 0
for i in range(m-1, -1, -1):
    tenBase += ABase[baseindex] * pow(A,i)
    baseindex += 1

BBase = []
if baseindex == 0:
    BBase.append(0)
else:
    while True:
        if tenBase // B == 0:
            BBase.append(tenBase)
            break
        else:
            BBase.append(tenBase%B)
        tenBase = tenBase // B
for i in range(len(BBase)-1, -1, -1):
    print(BBase[i], end=' ')
