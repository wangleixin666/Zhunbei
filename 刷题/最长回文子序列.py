# coding:utf-8

"""
    算法导论15.2
    字符串中最长回文子序列（子序列意思是不连续）
    输入：
    character
    输出：
    arac
    先写最长回文子串，连续的。。
    # 其实就是翻转后进行
"""


def longest_huiwen_chuan(a):
    # 暴力的解法
    # 用原字符串和倒置后的字符串求最长公共子串
    # 三个循环，两个指针，相等则同时移动两个指针，不相等移动后指针
    b = a[::-1]
    max_number = 0
    for index in range(len(a)):
        i = index
        j = 0
        number = 0
        while i < len(a) and j < len(a):
            if a[i] == b[j]:
                number += 1
                i += 1
            j += 1
            if number > max_number:
                max_number = number
    return max_number


if __name__ == '__main__':
    a = str(raw_input())
    print longest_huiwen_chuan(a)
