#BOJ 11652 카드
#딕셔너리를 이용한 풀이
import sys

N = int(sys.stdin.readline())

li = {}
for i in range(0,N):
    now = int(sys.stdin.readline())
    if li.get(now) == None:
        li[now] = 1
    else:
        li[now] += 1

max = 0
keyvalue = 0
first = True
for i in li:
    if first:
        max = li[i]
        keyvalue = i
        first = False
    if max < li[i]:
        max = li[i]
        keyvalue = i
    elif max == li[i] and keyvalue > i:
        keyvalue = i
print(keyvalue)