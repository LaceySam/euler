# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which, a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math


def generate_triplet(maximum: int) -> (int, int, int):
    for i in range(1, maximum):
        for j in range(1, maximum):
            if j < i:
                continue

            for k in range(1, maximum):
                if k < j:
                    continue

                if sum((i, j, k)) == maximum:
                    yield i, j, k


def is_pythagorian(i: int, j: int, k: int) -> bool:
    return (i*i + j*j) == k*k


def find_triplet(maximum: int) -> (int, int, int):
    for i, j, k in generate_triplet(maximum):
        if is_pythagorian(i, j, k):
            return i, j, k


if __name__ == '__main__':
    print(find_triplet(1000))
