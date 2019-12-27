N = int(input())

for i in range(0,N):
    for j in range(0, N-(i+1)):
        print(" ", end='')
    if i != N-1:
        for j in range(0, 2*i+1):
            if j==0 or j ==2*i:
                print("*", end='')
            else:
                print(" ",end='')
    else:
        for j in range(2*i+1):
            print("*", end='')
    print()
