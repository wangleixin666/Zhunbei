# -*- coding:utf-8 -*-
import sys

"""
2 4 7 9 8 5 2
10
"""


def find_b_in_a(a, b):
    # 利用dict数据结构，遍历两次，O(n)即可解决
    map = dict()
    for i in a:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
    for key, value in map.items():
        if b-int(key) in map:
            return key, b-int(key)
    return 'No'


if __name__ == '__main__':
    a = [int(x) for x in sys.stdin.readline().split()]
    b = int(input())
    print find_b_in_a(a, b)
