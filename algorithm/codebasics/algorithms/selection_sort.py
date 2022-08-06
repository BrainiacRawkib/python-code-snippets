def selection_sort_algo(arr):
    size = len(arr)

    for i in range(size - 1):
        min_index = i
        for j in range(min_index+1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 6, 8, 9],
        [34, 4, 2, 56, 89, 90],
        [234, 4, 1, 5, 99, 56, 34, 6, 80, 1233],
        [5]
    ]

    for test in tests:
        selection_sort_algo(test)
        print(test)
