"""Write a function that returns the highest value of array"""


def recursive_max(arr: list) -> int:
    if not arr:
        # considering the numbers will be integer positives
        return 0

    return max(arr[0], recursive_max(arr[1:]))


assert recursive_max([1, 2, 4, 1, 9, 0]) == 9
assert recursive_max([61, 2, 44, 111, 9, 2]) == 111
