# coding:utf-8
"""
    给一个已经排序好的数组，其中有的元素重复
    计算当中的不同元素个数，做Inplace的变换去重
    # 1,2,2,3,4,5,5,7,7
"""
import sys


def quchong(array):
    # 最笨的方法，但是要利用排好序这个条件
    result = []
    for i in array:
        if i not in result:
            result.append(i)
    return result


def quchong_1(array):
    # 排好序的话就考虑加个尾指针，减少循环次数
    i = 0
    result = []
    while i < len(array):
        result.append(array[i])
        j = i + 1
        while j < len(array) and array[j] == array[i]:
            j += 1
        i = j
    return result


"""
    算法题3：在一个无序数组中，寻找连续两个及两个以上的相同元素对的个数

    例如：有数组[10, 22, 32, 4, 4, 4, 5, 6, 9, 8, 8, 2, 2]，返回结果为3
    4， 4,  4
    8， 8
    2,  2
    算法题3延伸：如果给定的是一个有序数组，如何优化？
"""


def chongfudui_1(array):
    # 用一个for循环就解决了，但是有重复，可以存一下已经查找到的元素
    number = 0
    for i in range(len(array) - 1):
        if array[i + 1] == array[i]:
            if i == len(array) - 2 or array[i + 2] != array[i + 1]:
                number += 1
    return number


def chongfudui_2(array):
    number = 0
    array_1 = []
    # 这样实现就不用考虑边界问题
    for i in range(len(array) - 1):
        if array[i] in array_1:
            number += 1
        else:
            array_1.append(array[i])
    return number


def chongfudui_3(array):
    number = 0
    i = 0
    while i < len(array) - 1:
        j = i + 1
        while j < len(array) and array[j] == array[i]:
            # 当下一个元素和该元素相等，并且下下个元素不等时，数字对个数加一
            # 注意特殊情况就是没有下下个元素时的特殊情况
            if j == len(array) - 1 or array[j + 1] != array[j]:
                number += 1
            j += 1
        i = j
    return number


if __name__ == '__main__':
    array = [int(x) for x in sys.stdin.readline().split(',')]
    print chongfudui_3(array)
