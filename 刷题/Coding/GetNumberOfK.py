# coding:utf-8


def GetNumberOfK(data, k):
    return data.count(k)


if __name__ == '__main__':
    array = (1, 2, 3, 4, 4, 6)
    print GetNumberOfK(array, 4)