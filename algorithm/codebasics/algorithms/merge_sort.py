def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    print('entering...', left)
    print('len of left -->', len(left))
    merge_sort(left)
    print('After len of left -->', len(left))
    merge_sort(right)
    print('exiting...', left)
    merge_two_sorted_lists(left, right, arr)
    print('merging two arrays...', left)
    print(arr)
    print('\n\n')


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    # i = j = k = 0
    i = 0
    j = 0
    k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    merge_sort(arr)
    print(arr)

    # test_cases = [
    #     [10, 3, 15, 7, 8, 23, 98, 29],
    #     [],
    #     [3],
    #     [9, 8, 7, 6, 5, 4],
    #     [1, 2, 3, 4, 5, 6]
    # ]
    # for test_case in test_cases:
    #     merge_sort(test_case)
    #     print(test_case)
