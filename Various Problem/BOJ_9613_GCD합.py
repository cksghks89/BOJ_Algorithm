#BOJ 9613 GCD 합
import sys

def gcd(x,y):
    while (y > 0):
        tmp = x
        x = y
        y = tmp % y
    return x

def lcm(x,y):
    return int(x*y / gcd(x,y))

T = int(sys.stdin.readline())

for i in range(0, T):
    now = list(map(int, sys.stdin.readline().rstrip().split()))
    sum = 0
    for j in range(0, now.pop(0)-1):
        temp = now[j]
        for k in range(j+1,len(now)):
            sum += gcd(temp,now[k])

    print(sum)