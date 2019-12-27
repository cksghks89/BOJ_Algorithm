N = int(input())
list = []
for i in range(0,N+1):
    list.insert(i,[0]*(10))

for i in range(1,10):
    list[1][i] = 1

for i in range(2,N+1):
    list[i][0] = list[i-1][1]
    for j in range(1,9):
        list[i][j] = list[i-1][j-1]+list[i-1][j+1]
    list[i][9] = list[i-1][8]

sum = 0
for i in range(0,10):
    sum += list[N][i]
print(sum%1000000000)