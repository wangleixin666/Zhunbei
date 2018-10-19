# coding:utf-8

# 求整数n转换成二进制后1的个数

n = int(input())


def count_1(n):
    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n != 0:
        count += 1
        n = n & (n - 1)
    return count


def count_2(n):
    number = 0
    if n < 0:
        n = n & 0xffffffff
    while n != 0:
        number += (n % 2)
        n = n/2
    return number


print count_1(n)
print count_2(n)
