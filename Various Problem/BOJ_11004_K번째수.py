#BOJ 11004 K번째 수
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

A = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()
print(A[K-1])
