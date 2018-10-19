# coding:utf-8

"""
冒泡排序的实现：
    相邻两个元素比较，然后大的放后面，每次能把一个最大值确定位置，进行N-1次
"""


def maopaosort(list):
    for i in range(len(list)):
        for j in range(i, len(list)-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                """
                以上几行的交换两个元素的过程可以写成： 
                    list[j], list[j+1] = list[j+1], list[j]
                """
    return list


def maopaosort_1(list):
    """在冒泡排序的基础上加上一个岗哨，提前终止程序"""
    for i in range(len(list)):
        flag = 0
        for j in range(i, len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag += 1
                # flag代表交换操作执行的次数，每执行一次加1
        if flag == 0:
            # 判断如果整个内循环过程中没有执行交换操作，则表示数组已经完成了排序，可以跳出循环
            break
    return list


a = [1, 3, 7, 6, 5]
print maopaosort_1(a)
