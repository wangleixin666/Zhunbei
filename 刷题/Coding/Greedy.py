# coding:utf-8
# 实现贪心算法近似解决集合覆盖的NP难问题

state = ['mt', 'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az']
states_all = set(state)
# 利用python自带的set函数将list转化为没有交集的集合
# print type(states_all)
# 数据类型是集合

stations = dict()
# 将广播台清单用散列表表示
stations['kone'] = {'id', 'nv', 'ut'}
# python中集合和字典都用大括号表示，而且用set函数会提示警告
# set(['id', 'nv', 'ut'])，而且不是键值对，所以Python会识别为set类型的
# print type(stations['kone']) # <type 'set'>
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}

final_stations = set()
# 最后利用一个集合存储最终选择的广播台

"""贪心算法也就是每次选取覆盖最多的广播台，直到全部覆盖了"""
while states_all:
    # 当集合内元素不为空时，就不断查找能够覆盖最多的广播台，然后不断把覆盖的元素去除
    best_station = None
    states_covered = set()
    # 遍历所有的广播台，选择覆盖最多的广播台并存储到best_station
    for station, states_for_station in stations.items():
        # 因为stations是一个散列表，存储的是键值对，所以有两个循环参数
        covered = states_all & states_for_station
        # &代表集合取交集，|代表集合取并集，-代表取差集
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_all -= states_covered

print final_stations
# set(['ktwo', 'kthree', 'kone', 'kfive'])

