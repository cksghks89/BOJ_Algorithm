#BOJ 1676 팩토리얼 0의 개수
import sys

N = int(sys.stdin.readline())

ans = 1
for i in range(1, N+1):
    ans *= i
ans = list(str(ans))

num = 0
for i in range(len(ans)-1, -1, -1):
    if ans[i] != '0':
        break
    else:
        num += 1
print(num)