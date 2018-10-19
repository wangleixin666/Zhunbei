#!/usr/bin/env python    # -*- coding: utf-8 -*


def feibo(n):
    # 递归版本
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return feibo(n-1) + feibo(n-2)


def fib(n):
    # 用字典存储
    d = {}
    if n == 0:
        d[n] = 0
        return 0
    if n == 1:
        d[n] = 1
        return 1

    if not d.has_key(n):
        d[n] = fib(n-1) + fib(n-2)
    return d[n]


def fib2(n):
    # 用list存储
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2, n+1, 1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]


if __name__ == '__main__':
    print feibo(4)
    print fib(4)
    print fib2(0)
