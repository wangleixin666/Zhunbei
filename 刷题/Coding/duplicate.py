# coding:utf-8


def duplicate(numbers, duplication):
    set_ = set()
    for n in numbers:
        if n in set_:
            duplication[0] = n
            return True
        set_.add(n)
    return False


if __name__ == '__main__':
    array = (1, 2, 3, 4, 4, 6)
    print duplicate(3, array)
