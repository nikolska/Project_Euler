# Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import sympy


def sum_of_primes(number):
    '''
    Functions calculates the sum of all the primes below two million.
    :param int number: end range
    :return: number - the sum of prime numbers
    '''
    prime_list = list(sympy.primerange(1, number))
    return sum(prime_list)


if __name__ == '__main__':
    print(sum_of_primes(2000000))
