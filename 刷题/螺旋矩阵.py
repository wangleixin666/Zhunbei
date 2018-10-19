# coding:utf-8

"""
    作业帮提前批笔试
    输入5
    输出
    13 14 15 16 17
    12 3  4  5  18
    11 2  1  6  19
    10 9  8  7  20
    25 24 23 22 21
    输入4
    输出
    13 14 15 16
    12 3  4  5
    11 2  1  6
    10 9  8  7
    同理，n=1,2,3,4......n
    4个方向：
          →
        ↑   ↓
          ←
    每个方向都需要判断边界条件
"""


def zuoyebang(n):
    result = [[0 for i in range(n)] for j in range(n)]
    # 存储结果
    # 根据奇偶数判断输出结果，1的位置和结束的位置
    if n == 1:
        return 1
    if n % 2 == 0:
        # n是偶数的话
        a = b = n / 2
        # ab存储的是1的位置的横纵坐标
        result[a][b] = 1
        for i in range(1, a+1):
            l = 0
            while b + i + l > 0:
                # b+1+l
                result[a + i][b + i + l - 1] = result[a + i][b + i + l] + 1
                # 向左的都是a,a+1,a+2.....
                l -= 1
            u = 0
            while a + i + u > 0:
                result[a + i + u - 1][b + i + l] = result[a + i + u][b + i + l] + 1
                u -= 1
            r = 0
            while b + i + l + r < n - 1:
                result[a + i + u][b + i + l + r + 1] = result[a + i + u][b + i + l + r] + 1
                r += 1
            # 向下的少一次,最后一次跳过
            if i == a:
                break
            else:
                d = 0
                while a + i + u + d < n - 1:
                    result[a + i + u + d + 1][b + i + l + r] = result[a + i + u + d][b + i + l + r] + 1
                    d += 1

    # 确定1的位置
    # result[a][b-1] = 2
    # result[a-1][b-1] = 3
    # 第一次向左和向上是不全的，并不符合规律，所以先跳过
    else:
        # 奇数的情况下向左的多一次
        a = b = (n-1) / 2
        result[a][b] = 1
        for i in range(1, a + 1):
            l = 0
            while b + i + l > 0:
                # b+1+l
                result[a + i][b + i + l - 1] = result[a + i][b + i + l] + 1
                # 向左的都是a,a+1,a+2.....
                l -= 1
            u = 0
            while a + i + u > 0:
                result[a+i+u-1][b+i+l] = result[a+i+u][b+i+l] + 1
                u -= 1
            r = 0
            while b + i + l + r < n-1:
                result[a+i+u][b+i+l+r+1] = result[a+i+u][b+i+l+r] + 1
                r += 1
            d = 0
            while a + i + u + d < n-1:
                result[a+i+u+d+1][b+i+l+r] = result[a+i+u+d][b+i+l+r] + 1
                d += 1
        """
        i = a + 1
        l = 0
        while b + i + l > 0:
            # b+1+l
            result[a + i][b + i + l - 1] = result[a + i][b + i + l] + 1
            # 向左的都是a,a+1,a+2.....
            l -= 1
        """
        return result

"""分为4个方向，每个方向都有一个边界条件"""
# for i in range(1, 2):
# 从i=1开始的向左等等
# 这一部分增加是对的，接下来是关于不同方向的次数问题，因为不一定都是1次向左，1次向右，1次向下。。。
if __name__ == '__main__':
    n = int(input())
    print zuoyebang(n)


"""
顺序是先补全向左和向上的一部分
进行向左和向上的次数加1
然后进行循环，i从1开始
向右，向下，向左，向上，向右，向下。。。。。
次数的规律是分奇偶数的
奇数的时候向左的次数多一次，其余三个方向的次数均为a
偶数的时候乡下的的次数少一次，其余三个方向的次数均为a
注意起始位置并不是直接向左。。。是从补全完成后的向右开始。。。
"""
