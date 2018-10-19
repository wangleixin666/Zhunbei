# coding:utf_8


def OnlyOne(array):
    map = {}
    A = []
    for i in array:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    print map
    # 统计数组中数字出现的次数，存入字典中
    for j in map:
        if map[j] == 1:
            A.append(j)
    return A


if __name__ == '__main__':
    A = (1, 2, 2, 3, 4, 3, 2, 4, 5)

    print OnlyOne(A)
