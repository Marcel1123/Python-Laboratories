# Ex 2
def my_funct(*args, **kwargs):
    return sum(kwargs.values())


# Ex 3
def list_comp(text):
    return [i for i in text if i in ['o', 'a', 'i', 'i', 'o', 'i', 'u']]


# Ex 4
def fc(*args, **kwargs):
    result = []
    for i in args:
        if isinstance(i, dict):
            k = list(i.keys())
            if len(k) >= 2 and isinstance(k[-1], str):
                if len(k[-1]) >= 2:
                    result.append(i)
    return result


if __name__ == "__main__":
    my_f = lambda *args, **kwargs: sum(kwargs.values())
    list_cm = lambda text: list(filter(lambda i: i in ['o', 'a', 'i', 'i', 'o', 'i', 'u'], text))
    print(my_f(1, 2, c=3, d=4))
    print(list_cm("Programming in Python is fun"))
    print(fc({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
             dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
