#BOJ 10808 알파벳 개수

#a~z 97~122
import sys

S = sys.stdin.readline().rstrip()
alpha = [0 for i in range(0,26)]

for i in range(0, len(S)):
    alpha[ord(S[i])-97] += 1

for i in range(0, 26):
    print(alpha[i], end=" ")
