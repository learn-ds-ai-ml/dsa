"""problem solving techniques.

using two converging pointers to find unique pairs that equal to target sum.

"""

from typing import Callable

numbers = [1, 2, 2, 2, 2, 3, 4, 4, 5]


def find_pairs(total: int, lst: list[int]) -> list[tuple[int, int]]:
    """find the pair of indexes whose addition maches sum."""
    matches: list[tuple[int, int]] = []
    n = len(lst)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if lst[i] + lst[j] == total:
                matches.append((i, j))
    return matches


def find_pars_two_pointer(total: int, lst: list[int]) -> list[tuple[int, int]]:
    """Find pair of indexes whose sum is total."""
    matches: list[tuple[int, int]] = []
    indexed_list = sorted((value, idx) for idx, value in enumerate(lst))
    left = 0
    right = len(lst) - 1

    while left < right:
        pair_sum = indexed_list[left][0] + indexed_list[right][0]
        if pair_sum == total:
            matches.append((indexed_list[left][1], indexed_list[right][1]))
            # skipping duplicate numbers
            while left < right and indexed_list[left][0] == indexed_list[left + 1][0]:
                left += 1
            while left < right and indexed_list[right][0] == indexed_list[right - 1][0]:
                right -= 1
            left += 1
            right -= 1
        elif pair_sum < total:
            left += 1
        else:
            right -= 1
    return matches


# print(find_pairs(7, numbers))
print(find_pars_two_pointer(7, numbers))

# for i, num in enumerate(numbers, 2):
#     print(i, num)

# squares = [num ** 2 for num in numbers]
# print(squares)
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)
# grades = [55, 82, 67, 90]
# results = ['Pass' if g >= 60 else 'Fail' for g in grades]
# print(results)


def square(x: int) -> int:
    """Square the integer.

    Args:
        x(int): number

    Returns:
        (int): square of number
    """
    return x * x


square_lambda: Callable[[int], int] = lambda x: x * x

students = [("Zack", 20), ("Alice", 25), ("Bob", 22)]

by_age = sorted(students, key=lambda item: item[1])
