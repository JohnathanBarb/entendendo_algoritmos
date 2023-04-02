def quicksort(arr: list) -> list:

    if len(arr) < 2:
        return arr

    item = arr[0]
    higgers = []
    lowers = []
    for number in arr[1:]:
        if number <= item:
            lowers.append(number)
        else:
            higgers.append(number)

    return quicksort(lowers) + [item] + quicksort(higgers)


assert quicksort([3, 5, 6, 1, 2, 7, 4]) == [1, 2, 3, 4, 5, 6, 7]
assert quicksort([1]) == [1]
assert quicksort([]) == []
