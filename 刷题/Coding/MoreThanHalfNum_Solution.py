# coding:utf_8


def MoreThanHalfNum_Solution(numbers):
    map = {}
    for i in numbers:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    print map
    for j in map:
        if map[j] > len(numbers)/2:
            return j
    return 0


if __name__ == '__main__':
    A = (1, 2, 3, 2, 2, 2, 5, 4, 2)

    print MoreThanHalfNum_Solution(A)
