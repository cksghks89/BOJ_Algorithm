#BOJ 11651 좌표 정렬하기2

N = int(input())

li=[]

for i in range(0,N):
	a,b = map(int,input().split())
	li.append([b,a])

li.sort()

for i in range(0,N):
	print(li[i][1], li[i][0])