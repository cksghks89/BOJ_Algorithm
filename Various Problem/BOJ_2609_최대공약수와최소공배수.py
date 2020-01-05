#BOJ 2609 최대공약수와 최소공배수
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
print(gcd(A,B))
print(lcm(A,B))