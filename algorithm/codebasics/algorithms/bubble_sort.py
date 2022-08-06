def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp

                swapped = True
        if not swapped:
            break


def bubble_sort_2(elements, key):
    size = len(elements)
    outer_range = size - 1

    for i in range(outer_range):
        for j in range(outer_range - i):
            if elements[j][key] > elements[j + 1][key]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp


if __name__ == '__main__':
    elements = [5, 9, 3, 2, 1, 200, 67, 34, 88, 99, 45, 8]
    elements_2 = [1, 2, 3, 5, 6]

    # bubble_sort(elements)
    bubble_sort(elements_2)
    print(elements_2)

    elements_dict = [
        {'name': 'Ziyad', 'trans_amt': 1000},
        {'name': 'Ameer', 'trans_amt': 10000},
        {'name': 'Karim', 'trans_amt': 4500},
        {'name': 'Ahmed', 'trans_amt': 5400},
        {'name': 'Zaynab', 'trans_amt': 3500},
    ]

    # bubble_sort_2(elements_dict, 'name')
    bubble_sort_2(elements_dict, 'trans_amt')
    print(elements_dict)
