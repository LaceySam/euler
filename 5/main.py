# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?


def find_smallest_compound_divisor(ceiling: int) -> int:
    # Can omit 1 as everything is divisible by 1
    number_set = range(2, ceiling)

    # Start at ceiling for obvious reasons
    i = ceiling
    while True:
        # Could do a comprehension but this is way more efficient
        for number in number_set:
            if i % number:
                break

            if number == number_set[-1]:
                return i

        i += 1


if __name__ == '__main__':
    print(find_smallest_compound_divisor(20))
