def search_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = search_smallest(arr)
        new_arr.append(arr.pop(smallest_index))

    return new_arr


assert selection_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
assert selection_sort([1, 5, 10, 14, 14, 1]) == [1, 1, 5, 10, 14, 14]
