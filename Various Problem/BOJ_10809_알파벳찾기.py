#BOJ 10809 알파벳 찾기
# a~z 97~122
import sys

S = sys.stdin.readline().rstrip()
alpha = [-1 for i in range(0,26)]

for i in range(0, len(S)):
    now = ord(S[i])-97
    if alpha[now] == -1:
        alpha[now] = i
    else:
        pass

for i in range(0, 26):
    print(alpha[i], end=' ')