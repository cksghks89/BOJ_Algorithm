#BOJ 10430 나머지
import sys

A, B, C = map(int, sys.stdin.readline().split())

p1 = (A+B)%C
p2 = (A%C + B%C) % C
p3 = (A*B)%C
p4 = (A%C * B%C)%C
print(p1)
print(p2)
print(p3)
print(p4)