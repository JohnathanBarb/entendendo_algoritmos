from typing import Optional

def binary_search(array, item) -> Optional[int]:
    lower = 0
    higher = len(array) - 1

    while lower <= higher:
        middle = int((lower + higher) / 2)

        middle_item = array[middle]

        if middle_item == item:
            return middle

        if middle_item < item:
            lower = middle + 1
            continue
        
        higher = middle - 1

    return None


test_list = [1, 3, 5, 7, 9]


assert binary_search(test_list, 3) == 1
assert not binary_search(test_list, -1)

