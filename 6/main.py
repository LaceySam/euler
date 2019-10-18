# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640. Find the difference
# between the sum of the squares of the first one hundred natural numbers and
# the square of the sum.
import math


def calculate_sum_of_squares(ceiling: int) -> int:
    summed = 0
    for i in range(1, ceiling):
        summed += math.pow(i, 2)

    return int(summed)


def calculate_square_of_sums(ceiling: int) -> int:
    summed = sum(range(1, ceiling))

    return int(math.pow(summed, 2))


def calculate_sum_diff(ceiling: int) -> int:
    # Python and its range rules
    ceiling += 1
    return calculate_square_of_sums(ceiling) - calculate_sum_of_squares(ceiling)


if __name__ == '__main__':
    print(calculate_sum_diff(100))
