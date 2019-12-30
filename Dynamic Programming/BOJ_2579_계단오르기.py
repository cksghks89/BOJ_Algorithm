#BOJ 2579 계단오르기

N = int(input())
stair = [0 for i in range(0,N+1)]
dpList = [[0,0] for i in range(0,N+1)]

for i in range(0, N):
    stair[i] = int(input())

dpList[1] = [stair[0], 0]
dpList[2] = [stair[1], stair[0]+stair[1]]

for i in range(3, N+1):
    dpList[i] = [max(dpList[i-2])+stair[i-1], dpList[i-1][0]+stair[i-1]]

print(max(dpList[N]))