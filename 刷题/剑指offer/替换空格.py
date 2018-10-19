# coding:utf-8

"""
    请实现一个函数，将一个字符串中的每个空格替换成“%20”
    例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


def replaceSpace(s):
    new_s = ''
    for i in s:
        if i == ' ':
            new_s += '%20'
        else:
            new_s += i
    return new_s


def replaceSpace_1(s):
    # 剑指offer版本
    new_s = ''


if __name__ == '__main__':
    a = raw_input()
    print replaceSpace(a)
