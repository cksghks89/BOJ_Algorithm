X = int(input())

def dp_2(ci):
    list1 = [0,0,1,1]

    for i in range(4, X+1):
        i1 = i2 = i3 = 0
        if i % 3 == 0:
            i1 = int(i / 3)
        if i % 2 == 0:
            i2 = int(i / 2)
        i3 = i - 1

        if i1 != 0 and i2 != 0:
            min = list1[i1] if list1[i1] < list1[i2] else list1[i2]
            min = list1[i3] if list1[i3] < min else min
        elif i1 != 0 and i2 == 0:
            min = list1[i1] if list1[i1] < list1[i3] else list1[i3]
        elif i1 == 0 and i2 != 0:
            min = list1[i2] if list1[i2] < list1[i3] else list1[i3]
        else:
            min = list1[i3]
        list1.insert(i, min+1)

    return list1[X]
print(dp_2(X))