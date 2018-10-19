# coding:utf-8
# 选择排序，注意第一个函数返回的是下标，而不是直接返回数组中最小的元素是哪个
# 而数组在删除的时候
# 不过感觉用的是list不是tuple
"""注意Python中list和tuple的异同，进行比较"""


def findSamallest(arr):
    # 返回数组中最小元素的下标
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def SelectionSort(arr):
    new_array = []
    for i in range(len(arr)):
        smallest = findSamallest(arr)
        new_array.append(arr[smallest])
        arr.pop(smallest)
    return new_array


if __name__ == '__main__':
    arr = [3, 4, 5, 2, 1]
    print SelectionSort(arr)
