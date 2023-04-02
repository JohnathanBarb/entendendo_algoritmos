"""Write a recursive binary search function"""


def recursive_binary_search(arr: list, item: int, lower: int, higher: int) -> int | bool:

    if lower > higher:
        return False

    middle = int((lower + higher) / 2)

    if item == arr[middle]:
        return middle

    if arr[middle] > item:
        return recursive_binary_search(arr, item, lower, middle - 1)

    return recursive_binary_search(arr, item, middle + 1, higher)


test_list = [1, 3, 5, 7, 9]

assert recursive_binary_search(test_list, 3, 0, len(test_list)) == 1
assert not recursive_binary_search(test_list, -1, 0, len(test_list))
