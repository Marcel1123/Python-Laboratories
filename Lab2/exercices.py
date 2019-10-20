import itertools


# Ex 1
def fibonacci_number(number):
    fibonacci0 = 1
    fibonacci1 = 1
    fibonacci2 = 1
    for index in range(3, number + 1):
        fibonacci2 = fibonacci0 + fibonacci1
        fibonacci0 = fibonacci1
        fibonacci1 = fibonacci2
    return fibonacci2


def exercise_one():
    list_of_numbers = []
    input_number = input("Enter a number: ")
    if input_number.isnumeric() and int(input_number) >= 1:
        for index in range(1, int(input_number) + 1):
            list_of_numbers.append(fibonacci_number(index))
        return list_of_numbers
    else:
        return "Not a number. Or not a valid number.".split(" ")


# Ex 2
def is_prime(number):
    if number > 3:
        for index in range(2, int(number / 2) + 1):
            if number % index == 0:
                return False
    return True


def exercise_two(input_list):
    output = []
    for index in input_list:
        if is_prime(index):
            output.append(index)
    return output


# Ex 3
# Ex 4
def exercise_four(first_list, second_list):
    # INTERSECTION
    intersection = []
    for element_from_first in first_list:
        if second_list.count(element_from_first) > 0 and intersection.count(element_from_first) == 0:
            intersection.append(element_from_first)
    print("Intersection is: ", end="")
    print(intersection)

    # REUNION
    reunion = []
    for element_from_first_r in first_list:
        if reunion.count(element_from_first_r) == 0:
            reunion.append(element_from_first_r)
    for element_from_second_r in second_list:
        if reunion.count(element_from_second_r) == 0:
            reunion.append(element_from_second_r)
    print("Reunion is: ", end="")
    print(reunion)

    # FIRST MINUS SECOND
    first_minus_second = []
    for element_from_fr in first_list:
        if second_list.count(element_from_fr) == 0:
            first_minus_second.append(element_from_fr)
    print("First minus second: ", end="")
    print(first_minus_second)

    # SECOND MINUS FIRST
    second_minus_first = []
    for element_from_sc in second_list:
        if first_list.count(element_from_sc) == 0:
            second_minus_first.append(element_from_sc)
    print("Second minus first: ", end="")
    print(second_minus_first)


# Ex 5
def exercise_five(numbers, combination):
    print(list(itertools.combinations(numbers, combination)))


# Ex 6
def exercise_six(aparitii, *lists):
    result = []
    visited = []
    answer = 0
    for iterate in lists:
        for iterator in iterate:
            if str(iterator).isnumeric() and visited.count(iterator) == 0:
                for index in lists:
                    answer = answer + index.count(iterator)
            if answer == aparitii:
                visited.append(iterator)
                result.append(iterator)
            answer = 0

    print("Count fix: ", end="")
    print(result)


# Ex 7
def exercise_sept(x=1, flag=True, *strings):
    result = []
    id = 0
    for index in strings:
        result.append([])
        for character in index:
            if ord(character) % x != 0 and flag is False:
                result[id].append(character)
            elif ord(character) % x != 0 and flag is True:
                result[id].append(character)
        id += 1
    print(result)


# Ex 8


# Ex 9
def exercise_nine(tuples):
    # lst = len(tuples)
    # for i in range(0, lst):
    #     for j in range(0, lst - i - 1):
    #         if tuples[j][1][2] > tuples[j + 1][1][2]:
    #             temp = tuples[j]
    #             tuples[j] = tuples[j + 1]
    #             tuples[j + 1] = temp
    # print(tuples)
    print(sorted(tuples, key=lambda t: t[1][2]))

def f(k):
    return k%3
    # x = list(range(10))

    # print(sorted(x, key=f, reverse=True))


# if __name__ == "__main__":
#     print("Start program")
    # list_input = [1, 10, 12, 11]
    # list_input2 = [1, 5, 6, 9]
    # exercise_six(k, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
    # exercise_five([1, 2, 3, 4], 3)
    # exercise_sept(2, False, "test", "hello", "lab002")
    # exercise_nine([('abc', 'bcd'), ('abc', 'zza')])

    # x = {1:2, 2:3}
    # for el in x.items():
    #     x.keys()
    #     x.values()
    #     # print(x)

