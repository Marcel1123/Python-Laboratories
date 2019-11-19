# Ex 1
def first_last_name(list_of_name):
    return sorted(list_of_name, key=lambda a: a[1])


# Ex 2
def check_if_name_exist(list_of_tuples, name):
    for i in list_of_tuples:
        if i[1] == name:
            return True
    return False


# Ex 3
global_dict = {

    "+": lambda a, b: a + b,

    "*": lambda a, b: a * b,

    "/": lambda a, b: a / b,

    "%": lambda a, b: a % b

}


def apply_operator(operator, a, b):
    return global_dict[operator](a, b)


# Ex 4
global_funct = {

    "print_all": lambda *a, **k: print(a, k),

    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),

    "print_only_args": lambda *a, **k: print(a),

    "print_only_kwargs": lambda *a, **k: print(k)

}


def apply_funct(operator, *args, **kwargs):
    return global_funct[operator](args, kwargs)


# Ex 5
def dictionare_key(*args):
    result = dict()
    list = []
    for i in args:
        for k, v in i.items():
            if k not in result.keys():
                result[k] = v
            else:
                list.append((k, v))
    return result, list


# Ex 6
def ex6(recursive_dictionary, given_separator='-', recursive_string=""):
    for k, v in recursive_dictionary.items():
        if isinstance(v, dict):
            ex6(v, given_separator, recursive_string + k + given_separator)
        else:
            print(recursive_string, k, given_separator, v, sep="")


if __name__ == "__main__":
    print(check_if_name_exist(first_last_name([('ana', 'maria'), ('marcel', 'ionut')]), 'ionut'))
    print(apply_operator("*", 2, 2))
    print(apply_funct("print_all", 1, 2, 3, a=1, b=2))
    print(dictionare_key({1: 2, 2: 3, 5: 2, 6: 7}, {1: 4, 2: 5, 9: 0}, {3: 6, 0: 0}))
    ex6({'a': 1, 'b': {'c': 3, 'd': {'e': 5, 'f': 6}}})
