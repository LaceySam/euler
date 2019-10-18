# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(number: int) -> bool:
    # Seperate left from right
    _number = str(number)
    number_even = bool(len(_number) % 2 == 0)
    mid_point = round(len(_number) / 2)
    if number_even:
        mid_point -= 1

    left = ''
    right = ''
    for i, digit in enumerate(_number):
        if i < mid_point:
            left += digit

        elif i == mid_point:
            if number_even:
                left += digit

        else:
            right += digit

    return left == right[::-1]


def find_palindromes(digits: int) -> int:
    base = int('9' * digits)
    target = base
    palindromes = []

    while base:
        multiple = base * target
        if is_palindrome(multiple):
            palindromes.append(multiple)

        target -= 1
        if not target:
            target = int('9' * digits)
            base -= 1

    return max(palindromes)


if __name__ == '__main__':
    print(find_palindromes(3))
