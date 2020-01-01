#BOJ 2011 암호코드

code = list(input())
code = list(map(int, code))
code.insert(0,0)
dpList = [0 for i in range(0,len(code))]

boolean = False

dpList[0] = 1
if code[1] == 0:
    boolean = True
else:
    dpList[1] = 1

if len(code) >= 3:
    for i in range(2, len(code)):
        if code[i] == 0:
            if code[i-1] == 1 or code[i-1] == 2:
                dpList[i] = dpList[i-2]
            else:
                boolean = True
        elif 1 <= code[i] <= 6:
            if code[i-1] == 1 or code[i-1] == 2:
                dpList[i] = dpList[i-1] + dpList[i-2]
            else:
                dpList[i] = dpList[i-1]
        elif 7 <= code[i] <= 9:
            if code[i-1] == 1:
                dpList[i] = dpList[i-1] + dpList[i-2]
            else:
                dpList[i] = dpList[i-1]

if boolean:
    print(0)
else:
    print(dpList[len(code)-1]%1000000)