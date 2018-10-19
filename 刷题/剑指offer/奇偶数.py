# coding:utf-8

"""
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
    所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
import sys


def reOrderArray(array):
    array_ou = []
    array_ji = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array_ou.append(array[i])
        else:
            array_ji.append(array[i])
    array_ji.extend(array_ou)
    return array_ji


if __name__ == '__main__':
    array = [int(x) for x in sys.stdin.readline().split()]
    # 2 1 3 4 5 7
    print reOrderArray(array)
