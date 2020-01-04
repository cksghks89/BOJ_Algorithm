#BOJ 10845 큐
import sys

class queue:
    x = []

    def push(self, num):
        self.x.insert(len(self.x),num)
    def pop(self):
        if len(self.x) == 0:
            return -1
        else:
            rtn = self.x[0]
            self.x = self.x[1:]
            return rtn
    def size(self):
        return len(self.x)
    def empty(self):
        if len(self.x) == 0:
            return 1
        else:
            return 0
    def front(self):
        if len(self.x) == 0:
            return -1
        else:
            return self.x[0]
    def back(self):
        if len(self.x) == 0:
            return -1
        else:
            return self.x[len(self.x)-1]

N = int(sys.stdin.readline().rstrip())
Q = queue()

for i in range(0, N):
    command = sys.stdin.readline().rstrip()
    if command[:4] == "push":
        Q.push(command[5:])
    elif command[:5] == "front":
        print(Q.front())
    elif command[:3] == "pop":
        print(Q.pop())
    elif command[:4] == "size":
        print(Q.size())
    elif command[:4] == "back":
        print(Q.back())
    elif command[:5] == "empty":
        print(Q.empty())
