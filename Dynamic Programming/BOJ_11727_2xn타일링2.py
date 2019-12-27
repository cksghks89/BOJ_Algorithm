N = int(input())
list = [0]*(N+1)
list[1:3] = [1,3]
for i in range(3, N+1):
    list[i] = list[i-1]+2*list[i-2]
print(list[N]%10007)
