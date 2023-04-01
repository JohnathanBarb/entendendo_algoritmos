"""Write a recursive function that count amount of items in array"""


def recursive_count(arr: list) -> int:

    if not arr:
        return 0

    return 1 + recursive_count(arr[1:])


assert recursive_count([]) == 0
assert recursive_count([1, 1, 1, 1, 1, 1, 6])
assert recursive_count(["1", "teste", [], (1, 2, 3), 6]) == 5
