T = int(input())
for j in range(0,T):
    N = int(input())
    list = [0]*(N+1)
    list[1:4] = [1, 2, 4]
    for i in range(4,N+1):
        list[i] = list[i-1]+list[i-2]+list[i-3]
    print(list[N])
