#BOJ 10828 스택
import sys

class stack:
    X = []

    def push(self, num):
        self.X.insert(0,num)
    def pop(self):
        if len(self.X) == 0:
            return -1
        else:
            rtn = self.X[0]
            self.X = self.X[1:]
            return rtn
    def size(self):
        return len(self.X)
    def empty(self):
        if len(self.X) == 0:
            return 1
        else:
            return 0
    def top(self):
        if len(self.X) == 0:
            return -1
        else:
            return self.X[0]

sta = stack()
N = int(sys.stdin.readline().rstrip())
for i in range(0, N):
    command = sys.stdin.readline().rstrip()

    if command[0:4] == "push":
        sta.push(int(command[5:]))
    elif command[0:3] == "top":
        print(sta.top())
    elif command[0:4] == "size":
        print(sta.size())
    elif command[0:3] == "pop":
        print(sta.pop())
    elif command[0:5] == "empty":
        print(sta.empty())
