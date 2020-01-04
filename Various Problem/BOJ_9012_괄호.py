#BOJ 9012 괄호
import sys

class stack:
    x = []

    def push(self):
        self.x.insert(0, 1)
    def pop(self):
        if len(self.x) == 0:
            return -1
        else:
            rtn = self.x[0]
            self.x = self.x[1:]
            return rtn
    def clear(self):
        self.x = []

sta = stack()

N = int(sys.stdin.readline().rstrip())
for i in range(0, N):
    A = sys.stdin.readline().rstrip()
    t = False
    for j in range(0, len(A)):
        if A[j] == "(":
            sta.push()
        elif A[j] == ")":
            if sta.pop() == -1:
                t = True
                break
    if t == True or sta.pop() != -1:
        print("NO")
    else:
        print("YES")
    sta.clear()

