#BOJ 6588 골드바흐의 추측
import sys,math

prime = [0, 0]
for i in range(2, 1000001):
    prime.append(i)

for i in range(2, int(math.sqrt(1000000) + 1)):
    if prime[i] != 0:
        for j in range(2 * i, 1000001, i):
            prime[j] = 0
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    ba = 0
    t1 = t2 = 0
    for i in range(3, int(n/2)+1):
        if prime[i] != 0:
            for j in range(n, i-1,-1):
                if prime[j] != 0 and prime[i] + prime[j] < n:
                    break
                if prime[j] != 0 and prime[i]+prime[j] == n:
                    t1 = prime[i]
                    t2 = prime[j]
                    ba = -1
                    break
        if ba == -1:
            break
    if ba == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(str(n),"=",t1,"+",t2)