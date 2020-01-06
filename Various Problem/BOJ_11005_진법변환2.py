#BOJ 11005 진법 변환2
import sys
# A~Z 65~90

N, B = map(int,sys.stdin.readline().split())

t = 0
for i in range(1, 31):
    if N // pow(B, i) == 0:
        t = i
        break
ans = []

for i in range(t-1, 0, -1):
    temp = N // pow(B,i)
    N = N % pow(B,i)
    if temp >= 10:
        ans.append(chr(temp+55))
    else:
        ans.append(str(temp))
if N >= 10:
    ans.append(chr(N+55))
else:
    ans.append(str(N))
print(''.join(ans))
