#BOJ 10872 팩토리얼
import sys

N = int(sys.stdin.readline())

ans = N
for i in range(N-1,0,-1):
    ans *= i

if N == 0:
    print(1)
else:
    print(ans)