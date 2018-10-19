# coding:utf-8
# 采用字典创建图
# 接下来是创建队列实现广度优先搜索

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['peggy', 'annj']
graph['alice'] = ['peggy']
graph['claire'] = ['jonny']
graph['jonny'] = []
graph['peggy'] = []
graph['annj'] = []
"""
def find_seller(search_queue):
    # 利用队列的数据结构实现广度优先搜索
    def person_is_seller(name):
        return name[-1] == 'm'
    # print search_queue
    while search_queue:
        # 当搜索队列不为空时，等价于len(search_queue) != 0
        person = search_queue.popleft()
        # 弹出最左边的，也就是第一个进入队列的人，也就是第一次进入的，毕竟队列是先入先出的
        # 创建的队列还有很多方法，包括append,pop,reverse等常用的list方法
        if person_is_seller(person):
            print person + ' is seller'
            return True
        else:
            search_queue += graph[person]
            # 不然就更新队列，加入该节点的邻居，其中person为list中的一个元素
    print 'False'
    # 不过该函数有一个问题就是可能无线循环某个人，所以需要在检查完一个人后，标记他为已经检查过了，避免重复检查
"""


def find_seller(search_queue):
    # 利用队列的数据结构实现广度优先搜索
    def person_is_seller(name):
        return name[-1] == 'y'
    # print search_queue
    serched = []
    # 代表已经检查过的人的list
    while search_queue:
        # 当搜索队列不为空时，等价于len(search_queue) != 0
        person = search_queue.popleft()
        # 弹出最左边的，也就是第一个进入队列的人，也就是第一次进入的，毕竟队列是先入先出的
        # 创建的队列还有很多方法，包括append,pop,reverse等常用的list方法
        if person not in serched:
            # 当这个人没检查过时才进行检查，否则跳过这个人
            if person_is_seller(person):
                print person + ' is seller'
            else:
                search_queue += graph[person]
                # 不然就更新队列，加入该节点的邻居，其中person为list中的一个元素
            serched.append(person)
    return False
# 输出的结果太蠢了
# 还需要一点小修改，在没有结果时，输出什么，结果不唯一时输出什么
"""
Python中采用deque创建双端队列
利用队列实现广度优先遍历
"""
if __name__ == '__main__':
    from collections import deque
    # 创建双端队列

    queue = deque()
    # print queue
    # 创建好的空队列为：deque([])
    queue += graph['you']
    # print queue
    # 仅仅是把graph中you的邻居加入队列中了啊：
    # deque(['alice', 'bob', 'claire'])
    """但是如何实现二层遍历呢，就需要在函数中进行更新队列的操作了"""

    # print len(search_queue)
    # 3
    # queue.popleft()
    # print len(queue) # 2

    find_seller(queue)
