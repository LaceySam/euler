# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def sieve(number: int) -> int:
    i = 2
    top = number / 2
    largest_prime = 1
    previous_primes = []

    while True:
        if not number % i:
            # Check that number is not a multiple of previous prime

            if 0 not in [i % prime for prime in previous_primes]:
                previous_primes.append(i)
                largest_prime = i
                top = number / largest_prime

        if i >= top:
            return largest_prime

        i += 1


if __name__ == '__main__':
    print(sieve(600851475143))
