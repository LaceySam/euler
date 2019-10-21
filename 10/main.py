# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def sum_primes(maximum: int) -> int:
    # Start at 2 because 1 is not a valid prime
    prime_sum = 0
    numbers = range(2, maximum)
    prime_marker = [True] * maximum

    for i, number in enumerate(numbers):
        if not prime_marker[i]:
            continue

        prime_sum += number

        current = number * 2
        while current < maximum:
            prime_marker[current-2] = False
            current += number

    return prime_sum


if __name__ == '__main__':
    print(sum_primes(2000000))
