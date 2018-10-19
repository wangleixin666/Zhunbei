# coding=utf-8
"""
    输入abcdefghijklmnop
    输出abcde
        p   f
        o   g
        n   h
        mlkji
    螺旋矩阵
"""

import sys


def pdd_1(str):
    number = len(str)
    n = number / 4 + 1
    # 构造n*n的矩阵输出
    result = [[' ' for i in range(n)] for j in range(n)]
    result_1 = ''
    for i in range(n):
        result[0][i] = str[i]
    for l in range(n):
        result[l][n-1] = str[n-1+l]
    for j in range(n-1, -1, -1):
        result[n-1][j] = str[3*(n-1)-j]
    for k in range(n - 1, 0, -1):
        result[k][0] = str[4*(n-1)-k]
    # 输出矩阵形式的，然后换成字符串输出
    for b in range(n-1):
        for a in range(n):
            result_1 += result[b][a]
        result_1 += '\n'
    for a in range(n):
        result_1 += result[n-1][a]
    # return result
    return result_1

if __name__ == '__main__':
    a = sys.stdin.readline()
    print pdd_1(a)
