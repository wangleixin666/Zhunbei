def taijie(n):

    f = []
    f.append(0)

    for i in range(1, n+1, 1):
        f.append(2**(i-1))
    return f[n]


print taijie(2)
