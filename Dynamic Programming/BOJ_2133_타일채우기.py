#BOJ 2133 타일 채우기

N = int(input())

dpList = [0 for i in range(0,31)]
dpList[0] = 1
dpList[2] = 3
dpList[4] = 11

for i in range(6, N+1,2):
    dpList[i] = dpList[i-2]*3
    for j in range(4, i+1, 2):
        dpList[i] += 2*dpList[i-j]

if N % 2 == 1:
    print(0)
else:
    print(dpList[N])
