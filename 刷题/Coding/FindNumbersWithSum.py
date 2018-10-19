# coding:utf_8


def FindNumbersWithSum(array, tsum):
    if not array or not tsum:
        return []
    for i in array:
        cha = tsum - i
        if cha in array:
            return [i, cha]
    return []


if __name__ == '__main__':
    A = (1, 2, 4, 7, 11, 15)
    s = 15
    print FindNumbersWithSum(A, s)
