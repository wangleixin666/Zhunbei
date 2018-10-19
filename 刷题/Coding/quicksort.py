# coding:utf-8
# 快速排序的递归实现方法
# 还需要快排的非递归实现方法

"""
def quicksort(list):
    if len(list) < 2:
        return list
    privort = list[0]
    # 递归条件，选取的基准值
    less = []
    greater = []
    for i in list[1:]:
        if i < privort:
            less.append(i)
        greater.append(i)
    print 'less:'
    print less
    print 'greater:'
    print greater
    print 'result:'
    print quicksort(less) + [privort] + quicksort(greater)
    return quicksort(less) + [privort] + quicksort(greater)
    # [privort]要用list表示出来，否则不能把list和int类型的数据连接起来
输出结果为：[1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 5, 1, 2, 1]
"""


def quicksort(list):
    if len(list) < 2:
        return list
    privort = list[0]
    # 递归条件，选取的基准值
    less = []
    greater = []
    for i in list[1:]:
        if i <= privort:
            less.append(i)
        elif i > privort:
            # elif i > privort:
            # 还得加一个限制条件，而不是直接就是其他情况的话greater.append
            greater.append(i)
    return quicksort(less) + [privort] + quicksort(greater)
    # [privort]要用list表示出来，否则不能把list和int类型的数据连接起来


if __name__ == '__main__':
    list = [3, 4, 5, 2, 1]
    print quicksort(list)
