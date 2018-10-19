# coding:utf-8


class Node:
    def __init__(self, x):
        # 通过该初始化方法，声明链表的结构
        self.val = x
        # 存储数据
        self.next = None
        # 有一个指向下一个的指针


class Solution:
    def find_first_common_node(self, phead1, phead2):
        # 查找两个链表的第一个公共节点
        if not phead1 or not phead2:
            return None
        p1, p2 = phead1, phead2
        while p1 != p2:
            p1 = phead2 if not p1 else p1.next
            p2 = phead1 if not p2 else p2.next
        return p1


if __name__ == '__main__':
    # 实例化一个链表
    a = Node(0)
    b = Node(1)
    c = Node(2)
    a.next = b
    b.next = c
    # c.next不赋值的话就是初始的None，复合
    m = Node(1)
    n = Node(2)
    p = Node(3)
    m.next = n
    n.next = p

    print Solution.find_first_common_node(Solution(), a, m)

