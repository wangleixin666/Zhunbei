

def taijie(n):

    f = []
    f.append(0)
    f.append(1)
    f.append(2)

    for i in range(3, n+1, 1):
        f.append(f[i-1]+f[i-2])
    return f[n]


print taijie(3)
