n = int(input())
inputList = []

for i in range(0, n):
    inputList.append(int(input()))

if n == 1:
    print(inputList[0])
elif n == 2:
    print(inputList[0] + inputList[1])
else:
    dpList = [[0, 0] for i in range(0, n + 1)]
    dpList[1][1] = inputList[0]
    dpList[2][0] = dpList[1][1]
    dpList[2][1] = inputList[0] + inputList[1]

    for i in range(3, n + 1):
        max = 0
        sum1 = sum2 = 0
        sum1 = inputList[i - 1] + inputList[i - 2] + dpList[i - 2][0]
        sum2 = inputList[i - 1] + dpList[i - 1][0]
        max = sum1 if sum1 > sum2 else sum2
        dpList[i][1] = max
        dpList[i][0] = dpList[i - 1][1] if dpList[i - 1][1] > dpList[i - 1][0] else dpList[i - 1][0]

    print(dpList[n][0] if dpList[n][0] > dpList[n][1] else dpList[n][1])