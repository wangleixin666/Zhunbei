# -*- coding:utf-8 -*-


def Permutation(s):
    res = []
    if len(s) == 1:
        res.append(s)
    for i in range(len(s)):
        for j in Permutation(s[:i]+s[i+1:]):
            res.append(s[i]+j)
    return list(set(res))


if __name__ == '__main__':
    s = raw_input()
    print Permutation(s)

