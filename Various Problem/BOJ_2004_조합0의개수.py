#BOJ 2004 조합 0의 개수
import sys

def two(num):
    t1 = 2
    rtn = 0
    while t1 <= num:
        rtn += num // t1
        t1 *= 2
    return rtn

def five(num):
    t1 = 5
    rtn = 0
    while t1 <= num:
        rtn += num // t1
        t1 *= 5
    return rtn

n, m = map(int, sys.stdin.readline().split())

ans2 = 0
ans5 = 0

ans2 += two(n)
ans2 -= two(m)
ans2 -= two(n-m)

ans5 += five(n)
ans5 -= five(m)
ans5 -= five(n-m)

print(min(ans2, ans5))
