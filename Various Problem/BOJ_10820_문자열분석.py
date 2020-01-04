#BOJ 10820 문자열 분석
# A~Z 65~90  a~z 97~122  0~9 48~57  space 32
import sys

try:
    while True:
        now = input()
        p = [0,0,0,0]
        for i in range(0, len(now)):
            if 65 <= ord(now[i]) <= 90:
                p[1] += 1
            elif 97 <= ord(now[i]) <= 122:
                p[0] += 1
            elif 48 <= ord(now[i]) <= 57:
                p[2] += 1
            elif ord(now[i]) == 32:
                p[3] += 1
        print(p[0], p[1], p[2], p[3])
except: exit()