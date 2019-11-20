import math


def problema1():
    return 1+2+3+4+5+6+7+8+9+10


def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def problema2(n, m):
    ok = True
    aux = []
    while ok:
        o = m - 2*n
        if o <= 0 or o == n or o > n:
            return aux[-1], aux[-2]
        aux.append(o)
        m = n
        n = o


def problema3(m):
    res = []
    for i in range(1, m):
        if isPrime(i) and i < m:
            res.append(i)
    return res

def problema4(my_list):
    res = [i for i in my_list if isinstance(i, int)]
    return sorted(res, key=lambda k: k, reverse=True)


def problema5(n):
    sn = str(int(n, 8))
    if str(sn) == str(sn[::-1]):
        return True
    else:
        return False


def problema7(matrix):
    res = list(zip(*matrix))
    res1 = []
    for i in res:
        ok = 1
        for j in i:
            if i.count(j) >= 2:
                ok = 0
                break
        res1.append(ok)
    return res1


print(problema7([[1, 2], [1, 3]]))
