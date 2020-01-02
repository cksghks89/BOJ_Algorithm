#BOJ 2751 수 정렬하기2

N = int(input())
li = []

for i in range(0,N):
    now = int(input())
    li.append(now)

li.sort()
for i in range(0, N):
    print(li[i])
