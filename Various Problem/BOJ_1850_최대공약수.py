#BOJ 1850 최대공약수
import sys

def gcd(x,y):
    while (y > 0):
        tmp = x
        x = y
        y = tmp % y
    return x

def lcm(x,y):
    return int(x*y / gcd(x,y))

A, B = map(int, sys.stdin.readline().split())
T = gcd(A,B)
for i in range(0, T):
    print("1", end='')