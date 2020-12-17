# Consecutive prime sum
#
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?


# !!! work only if you know numbers 'below' and 'terms' !!!

import sympy


def prime_(below):
    prime_numbers = []
    n = 1
    while True:
        if sympy.isprime(n):
            if n < below:
                prime_numbers.append(n)
            else:
                break
        n += 1
    return prime_numbers


def prime_sum(below, terms):
    list_ = prime_(below)
    result = 0
    a, b = 0, terms
    while True:
        if result < sum(list_[a:b]):
            result = sum(list_[a:b])
        a += 1
        b += 1
        if result >= below:
            break
        print(result)


if __name__ == '__main__':
    prime_sum(1000000, 543)
