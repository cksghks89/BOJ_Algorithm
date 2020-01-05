#BOJ 1934 최소공배수
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
    A, B = map(int, sys.stdin.readline().split())
    print(lcm(A,B))
