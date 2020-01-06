#BOJ 1212 8진수 2진수
import sys

N = sys.stdin.readline().rstrip()

T = int(N, 8)
p = str(bin(T))
print(p[2:])