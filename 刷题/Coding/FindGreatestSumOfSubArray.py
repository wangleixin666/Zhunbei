# coding:utf-8


def FindSumOfSubArray(array):
    # 暴力求解
    max_now = array[0]
    pre = 0

    for i in array:
        if pre > i:
            pre += i
        else:
            pre = i

        if pre > max_now:
            max_now = pre

    return max_now

B = (-6, -3, -2, 1, -15)
print FindSumOfSubArray(B)

