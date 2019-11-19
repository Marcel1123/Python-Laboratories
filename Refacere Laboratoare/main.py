# L1
# Ex 1
import itertools
import math
from fractions import Fraction
from numbers import Number


def n_fibonacci_number(n):
    result = [0, 1]
    if n == 0:
        return result[0]
    elif n == 1:
        return result[1]
    else:
        while len(result) < n:
            result.append(result[len(result) - 2] + result[len(result) - 1])
    return result


# Ex 2
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prim_number_list(number_list):
    return [i for i in number_list if is_prime(i) is True]


# Ex 3
def ecuatia(lista):
    result = []
    for i in range(0, len(lista) - 1):
        for j in range(i, len(lista) - 1):
            panta = Fraction(lista[j][1] - lista[j][0], lista[i][1] - lista[i][0])
            result.append((panta.numerator, panta.denominator, -(-panta.denominator * lista[i][0] + panta.numerator * lista[i][1])))
    return result


# Ex 4
def list_operation(l1, l2):
    return set(l1) & set(l2), set(l1) | set(l2), set(l1) - set(l2), set(l2) - set(l1)


# Ex 5
def combinari(list_numbers, num):
    return list(itertools.combinations(list_numbers, num))


# Ex 6
def x_aparitii(*lists, x):
    result = []
    aux = []
    for i in lists:
        aux += i
    for i in aux:
        if isinstance(i, Number) and aux.count(i) == x and result.count(i) == 0:
            result.append(i)
    return result


# Ex 7
def str_chr(*strings, x=1, flag=False):
    return [[j for j in i if (flag is False and ord(j) % x != 0) or (flag is True and ord(j) % x == 0)] for i in strings]


# Ex 8
def tuple_din_liste(*lists):
    aux = list(lists)
    aux.sort(key=len, reverse=True)
    result = []
    for j in range(0, len(aux[0])):
        res = []
        for i in aux:
            if j >= len(i):
                res.append(None)
            else:
                res.append(i[j])
        result.append(tuple(res))
    return result


# Ex 9
def tuple_sort(lists):
    return sorted(lists, key=lambda tup: tup[1][2])


if __name__ == "__main__":
    # print(n_fibonacci_number(10))
    # print(prim_number_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # print(combinari([1, 2, 3, 4], 3))
    # print(x_aparitii([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))
    # print(str_chr("test", "hello", "lab002", x=2, flag=False))
    # print(tuple_din_liste([1, 2, 3], [5, 6, 7, 1, 1], ["a", "b", "c"]))
    # print(tuple_sort([('abc', 'bcd'), ('abc', 'zza')]))
    print(ecuatia([(1, 2), (5, 6), (5, 9)]))
