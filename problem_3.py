# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import sympy


def divisor(number):
    '''
    Function finds the largest prime factor of some number
    :param int number: some number
    :return: the largest prime factor
    '''
    prime_numbers = [i for i in range(1, number) if sympy.isprime(i)]
    list_divisors = [i for i in prime_numbers if number % i == 0]
    return max(list_divisors)


if __name__ == '__main__':
    print(divisor(600851475143))
