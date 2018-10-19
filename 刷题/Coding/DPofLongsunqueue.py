# coding:utf-8
# 采用动态规划DP算法解决
# 1、最长公共子串的问题
# 2、最长公共子序列

"""动态规划仅适用于子问题是离散的情况，且不依赖于其他子问题时，独立且离散才可以"""


def longsubqueue(a, b):
    # 求两个字符串相同的位数，不过时间复杂度也很高
    cell = [[0 for col in range(len(a))] for row in range(len(b))]
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                cell[i][j] = 0
    # print cell
    # 输出的就是画的表格，输出最后一行最后一列的结果就好了
    return cell[len(a) - 1][len(b) - 1]


def longsub(a, b):
    # 求两个字符串最长公共子序列，也就是次序也要一致
    cell = [[0 for col in range(len(a))] for row in range(len(b))]
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    # print cell
    # 输出的就是画的表格，输出最后一行最后一列的结果就好了
    return cell[len(a) - 1][len(b) - 1]

print longsub('fish', 'hsih')
