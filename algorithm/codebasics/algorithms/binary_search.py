from utils import time_it


@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


@time_it
def binary_search_algo(numbers_list, number_to_find):
    left_index = 0
    right_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def binary_search_recursion(numbers_list, number_to_find, left_index, right_index):

    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2

    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursion(numbers_list, number_to_find, left_index, right_index)


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 15

    # numbers_list = [i for i in range(1000001)]
    # number_to_find = 100000

    linear_search_time = linear_search(numbers_list, number_to_find)

    binary_search_time = binary_search_algo(numbers_list, number_to_find)

    numbers_list_2 = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find_2 = 15

    index = binary_search_recursion(numbers_list_2, number_to_find_2, 0, len(numbers_list_2))
    print(f'Number found at index {index} using binary search')
