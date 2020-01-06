#BOJ 2745 진법 변환
import sys

N, B = sys.stdin.readline().split()
B = int(B)
print(int(N,B))