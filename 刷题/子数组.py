# coding:utf-8
"""
A=【1，2，3，5，8，7，6，5，9，1，1，6，9，8】
B=【5，8，7】
在A中找到子数组B

# 最笨的方法，遍历，然后可以用KMP字符串匹配

在A中找出B，元素必须是连续的（也就是在A中找出连在一起的5，8，7）
返回符合这种情况的B的第一个元素在A的位置（也就是5的位置，第3位）
如果没有，返回一个负数；
"""
import sys


def subarray(A, B):
    for i in range(len(A)):
        j = 0
        m = i
        while j < len(B):
            if A[m] == B[j]:
                j += 1
                m += 1
            else:
                break
        if j == len(B):
            return i
    return -1


if __name__ == '__main__':
    A = [int(x) for x in sys.stdin.readline().split(',')]
    B = [int(x) for x in sys.stdin.readline().split(',')]
    print subarray(A, B)

