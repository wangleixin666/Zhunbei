# coding=utf-8


def find(s):
    array = [s[i:] for i in range(len(s))]
    array.sort()
    r = ''
    max_r = 0
    for i in range(len(array) - 1):
        a = array[i]
        b = array[i+1]
        lens = min(len(a), len(b))
        cnt = 0
        for j in range(lens):
            if a[j] == b[j]:
                cnt += 1
        if max_r < cnt:
            max_r = cnt
            r = a[:cnt]
    return len(r)


if __name__ == '__main__':
    a = raw_input()
    print find(a)
