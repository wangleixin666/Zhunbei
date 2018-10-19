# coding:utf-8

"""
    输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""
import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printListFromTailToHead(listNode):
    # write code here
    """
    result = []
    while listNode:
        result.append(listNode.val)
        listNode = listNode.next
    return result[::-1]
    """
    """
    if listNode == None:
        return []
    return self.printListFromTailToHead(listNode.next) + [listNode.val]
    """

    res = []
    if listNode is None:
        return []
    while listNode is not None:
        res.append(listNode.val)
        listNode = listNode.next
    # res.insert(0,listNode.val)
    # 每次插入到队首，也就是实现了逆序
    res.reverse()
    return res


if __name__ == '__main__':
    a = int(input())
    head = ListNode(a)
    p = head
    data = [int(x) for x in sys.stdin.readline().split()]

    for x in data[:]:
        node = ListNode(x)
        # 注意下面两句话的顺序，不要弄颠倒，首先要让p指向node，然后再把它重新赋值给p，这样才完成了对p的更新
        p.next = node
        p = p.next

    list = []
    while head is not None:
        list.insert(0, head.val)
        head = head.next
    # list.reverse()
    print list