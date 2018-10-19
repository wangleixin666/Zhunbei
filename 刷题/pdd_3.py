# coding=utf-8
import sys
"""
第一个数字为人的个数，第二个数字为要求的序号
找出不是直接认识的朋友，但是共同朋友最多的序号
即：不是0的朋友，但是共同好友最多，也就是4
5 0
1 2 3
0 4
0 4
0 4
1 2 3
"""


def pdd_3(graph, n, k):
    list_1 = []
    new_graph = []
    new_graph.append(k)
    for i in range(len(graph[k])):
        new_graph.append(int(graph[k][i]))
    for i in range(n):
        if i not in new_graph:
            list_1.append(i)
    max_length = 0
    max_index = -1
    for m in list_1:
        # 代表着不是它的直接朋友
        list_m = []
        # 存放两者的交集，然后找到交集最大的一组就可以了
        for j in graph[k]:
            list_m.append(j)
            if j in graph[m]:
                list_m.append(j)
        list_m_1 = set(list_m)
        if len(list_m_1) > max_length:
            max_index = m
    return max_index


if __name__ == '__main__':
    n, k = sys.stdin.readline().split()
    graph = dict()
    k = int(k)
    n = int(n)
    result = []
    for i in range(n):
        graph[i] = sys.stdin.readline().split()
    print pdd_3(graph, n, k)
