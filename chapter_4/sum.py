"""Write a recursive function that sums a list of ints"""


def recursive_sum(arr: list[int]) -> int:
    if not arr:
        return 0

    return arr[0] + recursive_sum(arr[1:])


assert recursive_sum([1, 2, 3, 4]) == 10
assert recursive_sum([10, 20, 43, 56, 11]) == 140
assert recursive_sum([]) == 0
