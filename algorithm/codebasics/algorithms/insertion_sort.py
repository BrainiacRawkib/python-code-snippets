def insertion_sort_algo(elms):
    for i in range(1, len(elms)):
        anchor = elms[i]
        j = i - 1

        while j >= 0 and anchor < elms[j]:
            print('first inner j ->', j)
            elms[j + 1] = elms[j]
            j = j - 1
        elms[j + 1] = anchor


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort_algo(elements)
    print(elements)

    tests = [
        [11, 9, 29, 7, 2, 15, -28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for test in tests:
        insertion_sort_algo(test)
        print(f'Sorted array: {test}')
