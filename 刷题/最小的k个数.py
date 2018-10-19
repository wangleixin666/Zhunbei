# -*- coding:utf-8 -*-

"""
    找出数组中最小的k个数并输出
    按照快排的思想，random_select思想，找到第五小的数，在它之前的四个数输出为result
    堆排序的思想，找最小的，只需要建立前k个数的最大堆O(lgk)，然后遍历n个数
    全排序，然后输出前k个最小的数
"""
import sys


def quick_partion(arr, pivotIndex):
    index = 0
    r = len(arr) - 1
    pivotValue = arr[pivotIndex]
    arr[pivotIndex], arr[r] = arr[r], arr[pivotIndex]
    for i in range(0, r + 1):
        if arr[i] < pivotValue:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    arr[index], arr[r] = arr[r], arr[index]
    return index


def pivot_median(arr):
    n = len(arr)
    while n > 5:
        cols = n/5
        m = []
        for i in range(0, cols):
            s = sorted(arr[5*i:(5*i+5)])
            m.append(s[2])
        arr = m
        n = len(arr)
    arr.sort()
    return arr[n/2]


def bfprt(arr, k):
    pivot = pivot_median(arr)
    pivotIndex = arr.index(pivot)
    index = quick_partion(arr, pivotIndex)
    n = len(arr)
    if k < n - index:
        return bfprt(arr[index+1:n], k)
    elif k == n - index:
        return pivot
    elif k > n - index:
        return bfprt(arr[0:index], k-(n-index))


if __name__ == '__main__':
    array = [int(x) for x in sys.stdin.readline().split()]
    k = int(input())
    # 第k小的元素
    # 2 4 5 1 6 3
    print quick_partion(array, k)

