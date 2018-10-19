# coding:utf-8
# 求list中所有元素的和，两种方法
# 分治算法求列表中最大的数字


def sumofList1(arr):
    # 返回数组中最小元素的下标
    total = 0
    for i in arr:
        total += i
    return total


def sumofList2(arr):
    # 采用分治的思想，不断缩小问题的规模
    if len(arr) == 0:
        sum = 0
    else:
        sum = arr[0] + sumofList2(arr[1:])
    return sum


def maxofList(list):
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        return list[1]
    sub_max = maxofList(list[1:])
    if list[0] > sub_max:
        return list[0]
    return sub_max

if __name__ == '__main__':
    arr = [3, 4, 5, 2, 1]
    print maxofList(arr)
