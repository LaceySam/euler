# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13. What is the 10 001st prime number?


def check_prime(number: int, primes: list = None) -> bool:
    if not primes:
        primes = []

    # Go through all previously found primes and do a mod, if divisible not
    # a prime
    for prime in primes:
        if not number % prime:
            return False

    return True


def sieve(prime_number_position: int) -> int:
    primes = []

    # Start at 2 because 1 is not a valid prime
    i = 2
    count = 0

    while True:
        prime = check_prime(i, primes)
        if prime:
            primes.append(i)
            count += 1
            if count == prime_number_position:
                return i

        i += 1

if __name__ == '__main__':
    print(sieve(10001))
