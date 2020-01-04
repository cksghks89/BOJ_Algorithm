#BOJ 1406 에디터
import sys
string = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())

cursorLeft = list(string)
cursorRight = []

for i in range(0, N):
    command = sys.stdin.readline().rstrip()
    if command[0] == "L" and len(cursorLeft) != 0:
        cursorRight.append(cursorLeft.pop())
    elif command[0] == "D" and len(cursorRight) != 0:
        cursorLeft.append(cursorRight.pop())
    elif command[0] == "B" and len(cursorLeft) != 0:
        cursorLeft.pop()
    elif command[0] == "P":
        cursorLeft.append(command[2:])

sys.stdout.write(''.join(cursorLeft+cursorRight[::-1]))
