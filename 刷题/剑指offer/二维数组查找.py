# coding:utf-8

"""
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
import sys


def Find(target, array):
    # 暴力求解的办法，遍历整个二维数组
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if array[i][j] == target:
                return True
    return False


def Find_1(target, array):
    # 递归求解，最后一列第一个为该列最小值
    # 从右上角向下
    rows = len(array) - 1
    # 行数
    cols = len(array[0]) - 1
    # 列数
    i = 0
    j = cols
    while j >= 0 and i <= rows:
        if target < array[i][j]:
            j -= 1
            # 比右上角元素小，去除该列
        elif target > array[i][j]:
            i += 1
            # 比右上角元素大，去除该行
        else:
            return True
    return False


if __name__ == '__main__':
    target = int(input())
    n = int(input())
    array = []
    for i in range(n):
        lines = [int(x) for x in sys.stdin.readline().split()]
        array.append(lines)
    print Find_1(target, array)
"""
11
3
2 3 4
5 6 7
8 9 10
"""
