# coding:utf-8

# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）


def Sum_Solution(n):
    # write code here
    ans = n
    temp = ans and Sum_Solution(n - 1)
    ans = ans + temp
    return ans


if __name__ == '__main__':
    n = int(input())
    print Sum_Solution(n)
