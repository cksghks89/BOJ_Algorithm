a = int(input())

for b in range(a, 0, -1):
    for y in range(0,a-b):
        print(" ", end='')
    for x in range(0,b):
        print("*", end='')
    print()