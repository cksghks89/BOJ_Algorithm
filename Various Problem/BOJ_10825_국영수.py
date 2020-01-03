#BOJ 10825 국영수

N = int(input())

li = []

for i in range(0, N):
	a,b,c,d = input().split()
	li.append([a, int(b), int(c), int(d)])

li.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(0,N):
	print(li[i][0])
