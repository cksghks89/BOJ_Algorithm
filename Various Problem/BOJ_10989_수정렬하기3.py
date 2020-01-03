#BOJ 10989 수 정렬하기3
import sys
N = int(sys.stdin.readline())
li = [0]*10001
for i in range(0, N):
	li[int(sys.stdin.readline())] += 1

for i in range(0,10001):
	for j in range(0,li[i]):
		print(i)