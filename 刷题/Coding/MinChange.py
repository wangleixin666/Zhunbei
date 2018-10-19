# coding:utf-8

"""
    要求出改变最小绝对值的上升数组
    1,3,2,2,1,5,4
    确保整体上升，但允许重复，改变的绝对值最小
    1,2,2,2,2,4,4绝对值之和为0+1+0+0+1+1+0=3
    没有更小的数组了
    动态规划，前一列小于等于j中最小值加a[i]-j
"""


def min_change(a):
    b = list(set(a))
    # b存放a的所有值，从最小到最大
    A = [[0 for i in range(len(a))] for j in range(len(b))]
    # A是存放最小值的矩阵，大小为len(b)*len(a),初始化为全0的，方便计算
    # 此处为5行7列的矩阵，5行为b的取值，7列为数组长度
    # 第一列为初始值0，然后动态规划
    result = []
    result.append(b[0])
    # 用来存放最终的结果
    # 肯定从最小值起始，所以后面第一列为全0
    for j in range(1, len(a)):
        for i in range(len(b)):
            # i代表行，j代表列
            min_number = A[0][j-1]
            for k in range(0, i+1):
               if A[k][j-1] < min_number:
                   min_number = A[k][j-1]
            A[i][j] = min_number + abs(a[j] - b[i])
            # 每一个值为前一列位于该行上方所有值的最小加上绝对值之差
    # print A
    # [[0, 2, 3, 4, 4, 8, 11], [0, 1, 1, 1, 2, 5, 7], [0, 0, 1, 2,
    # 3, 4, 5], [0, 1, 2, 3, 4, 3, 3], [0, 2, 3, 4, 5, 2, 3]]
    # 此时A的最后一位元素为最小的绝对值之和//不一定，但是最小值为最后一列的最小，然后反向求出数组即可

    return A

a = [1, 3, 2, 1, 1, 5, 4]
print min_change(a)
