# coding:utf-8
# 实现有向无环非负加权图
# 然后实现迪杰斯特拉算法求最短加权路径

"""需要几个散列表，分别是图graph，花费costs，父节点parents"""

graph = dict()
graph['start'] = dict()
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = dict()
graph['a']['fin'] = 1
# 对该图中的节点也是散列表
graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = dict()
# print graph['start'].keys()
# 上述代码实现了一个有向加权图

costs = dict()
costs['a'] = 6
costs['b'] = 2
infinity = float('inf')
# 代表无穷大的花费
costs['fin'] = infinity
"""该花费散列表表示从起点到此处的花费，因为无法直接到终点，所以是无穷大"""

parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
"""该散列表表示的各个节点的父节点，方便采用Dijkstra找到最小花销后倒序返回最短路径"""

processed = []
# 表示已经更新过权值的节点，避免重复处理


def find_lowest_cost_node(costs):
    # 找到花销最小的节点
    lowest_cost = float('inf')
    # 先初始化为无穷大
    lowest_cost_node = None
    # 初始化为不存在
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost:
            lowest_cost_node = node
            lowest_cost = cost
    return lowest_cost_node


node = find_lowest_cost_node(costs)
# 在未处理的节点中找到开销最小的节点

if node not in processed:
    # 加上这个判断条件，不然可能造成死循环了
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            # 不断更新所有邻居的花销，更新costs散列表
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    # 随着costs的更新，也不断更新要查找的花销最少的节点node
print costs

"""
迪杰斯特拉算法分为以下四步：
    1、找到花销最少的节点
    2、计算前往各个邻居节点的花销，判断是否需要更新花销
    3、重复进行上述过程，直到图中所有节点都已经计算完成
    4、计算最终结果
"""