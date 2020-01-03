#BOJ 11650 좌표 정렬하기

N = int(input())

li = []

for i in range(0,N):
	li.append(list(map(int, input().split())))

li.sort()

for i in range(0,N):
	print(li[i][0],li[i][1])