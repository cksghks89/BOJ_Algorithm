#BOJ 11655 ROT13

# A~Z 65~90  a~z 97~122

S = list(input())
for i in range(0,len(S)):
    if 65 <= ord(S[i]) <= 90:
        S[i] = chr((ord(S[i])-65+13)%26 + 65)
    elif 97 <= ord(S[i]) <= 122:
        S[i] = chr((ord(S[i])-97+13)%26 + 97)

for i in range(0, len(S)):
    print(S[i], end='')
