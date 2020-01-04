#BOJ 10799 쇠막대기
import sys

pipe = []
T = list(sys.stdin.readline().rstrip())
number = 0
for i in range(0, len(T)):
    if T[i] == "(" and T[i+1] == ")":
        for i in range(0, len(pipe)):
            pipe[i] += 1
    elif T[i] == "(":
        pipe.insert(0,0)
    elif T[i] == ")" and T[i-1] != "(":
        number += pipe[0]+1
        pipe = pipe[1:]

print(number)