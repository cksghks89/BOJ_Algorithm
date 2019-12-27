N = int(input())

for x in range(N,0,-1):
    for y in range(0,x):
        print("*", end='')
    print()