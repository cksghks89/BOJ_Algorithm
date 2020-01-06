#BOJ 1373 2진수 8진수
import sys

N = sys.stdin.readline().rstrip()

T = int(N, 2)
p = str(oct(T))
print(p[2:])