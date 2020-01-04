#BOJ 10656 접미사 배열

S = input()

li = []
for i in range(0,len(S)):
    li.append(S[i:])
li.sort()
for i in range(0, len(S)):
    print(li[i])
