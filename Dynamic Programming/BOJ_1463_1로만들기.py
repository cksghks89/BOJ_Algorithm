N = int(input())

def tile(n):
    list = [0]*(N+1)

    list.insert(0,0)
    list.insert(1,1)
    list.insert(2,2)

    for i in range(3,n+1):
        list[i] = list[i-1]+list[i-2]
    return list[n]

print(tile(N)%10007)