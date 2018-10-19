# coding:utf-8

f = [f for f in (lambda x: x, lambda x: x ** 2)]
#  f = [f for f in (lambda x: x, lambda x: x ** 2) if f(1) == 1]
# 后面的if表达式没什么用？？？
print(f)
# [<function <lambda> at 0x000000000268A9E8>, <function <lambda> at 0x000000000268AA58>]
print(f[0](2))
# f[0]表示按照第一个规则返回x
# 返回：2
print(f[1](2))
# f[1]表示按照第二个规则返回x**2
# 返回4
g = lambda x: x + 1
print g(2)
# 返回3

a = [2, 3, 1, 4, 5, 7]
a_1 = sorted(a)
a.sort(reverse=True)
print a_1
print a

# 能够直接用lambda表达式表示出来结果
a = [(3, 2), (3, 4), (1, 5)]


def compare(array_1, array_2):
    if array_1[0] < array_2[0]:
        return True
    elif array_1[0] > array_2[0]:
        return False
    else:
        if array_1[1] >= array_2[1]:
            return True
        elif array_1[1] < array_2[1]:
            return False


def sort_cmp(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if compare(array[j], array[i]):
                array[j], array[i] = array[i], array[j]
    return array

print sort_cmp(a)
