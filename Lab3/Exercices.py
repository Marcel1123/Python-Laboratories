def function1(first_list, second_list):
    response = [set(first_list) | set(second_list), set(first_list) & set(second_list),
                set(first_list) - set(second_list), set(second_list) - set(first_list)]
    return set(frozenset(i) for i in response)
    # return set(first_list) | set(second_list), set(first_list) & set(second_list),
    #             set(first_list) - set(second_list), set(second_list) - set(first_list)


def function2(my_string):
    dictionary = dict()
    cnt = 0
    for leter in my_string:
        cnt = my_string.count(leter)
        dictionary[leter] = cnt
        my_string.translate({ord(leter): None})
    return dictionary


def function4(tag_name, text_content, href, css_class_name):
    return "<%s %s %s >%s</%s>" % (tag_name, href, css_class_name, text_content, tag_name)


def function6(set_input):
    return len(set_input), 0


if __name__ == "__main__":
    # print(function2("ASdqwe12wE!W!2xw2!qwewq"))
    # print(function1([1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 8]))
    print(function6({1, 2, 4, 3, 5, 1, 5, 1, 24, 3}))
