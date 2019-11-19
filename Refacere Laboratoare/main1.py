# Ex 1
def list_operation(l1, l2):
    res = [list(set(l1) & set(l2)), list(set(l1) | set(l2)), list(set(l1) - set(l2)), list(set(l2) - set(l1))]
    return set(frozenset(i) for i in res)


# Ex 2
def get_leter_aparitii(string):
    result = dict()
    for i in string:
        result[i] = string.count(i)
        string.replace(i, "")
    return result


# Ex 5
def validate_dict(sets, dicts):
    for key in dicts:
        find_rule = list(filter(lambda a: a[0] is key, sets))
        if len(find_rule) == 1:
            text = dicts[key]
            if text.startswith(find_rule[0][1]) and text.endswith(find_rule[0][3]) and text.count(find_rule[0][2]) > 0:
                continue
            else:
                return False
        else:
            return False
    return True


# Ex 6
def set_troll(sets):
    return len(sets), 0


# Ex 7
def set_operator(set1, set2):
    result = dict()
    result[set1.__str__() + '|' + set2.__str__()] = len(set1 | set2)
    result[set1.__str__() + '&' + set2.__str__()] = len(set1 & set2)
    result[set1.__str__() + '-' + set2.__str__()] = len(set1 - set2)
    result[set2.__str__() + '-' + set1.__str__()] = len(set2 - set1)
    return result


if __name__ == "__main__":
    print(list_operation([1, 2, 3, 4, 5, 6], [1, 2, 8, 9]))
    print(get_leter_aparitii("Ana has apples."))
    print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                        {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
    print(set_operator({1, 2}, {2, 3}))
