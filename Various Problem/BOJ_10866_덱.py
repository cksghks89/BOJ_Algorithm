#BOJ 10866 덱
import sys

class deque:
    x = []

    def push_front(self, num):
        self.x.insert(0, num)
    def push_back(self, num):
        self.x.insert(len(self.x), num)
    def pop_front(self):
        if len(self.x) == 0:
            return -1
        else:
            return self.x.pop(0)
    def pop_back(self):
        if len(self.x) == 0:
            return -1
        else:
            return self.x.pop(len(self.x)-1)
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
dQ = deque()

for i in range(0, N):
    com = sys.stdin.readline().rstrip()
    if com[:4] == "size":
        print(dQ.size())
    elif com[:4] == "back":
        print(dQ.back())
    elif com[:5] == "front":
        print(dQ.front())
    elif com[:5] == "empty":
        print(dQ.empty())
    elif com[:8] == "pop_back":
        print(dQ.pop_back())
    elif com[:9] == "pop_front":
        print(dQ.pop_front())
    elif com[:9] == "push_back":
        dQ.push_back(com[10:])
    elif com[:10] == "push_front":
        dQ.push_front(com[11:])
