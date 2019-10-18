# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
# multiples of 3 or 5 below 1000.


def find_multiples(numbers: list, ceiling: int) -> list:
    if not numbers:
        return 0

    multiple_sum = 0
    for i in range(1, ceiling):
        if 0 in ([i % number for number in numbers]):
            multiple_sum += i

    return multiple_sum


if __name__ == '__main__':
    print(find_multiples([3, 5], 1000))
