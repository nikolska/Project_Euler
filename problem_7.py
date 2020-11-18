# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import sympy


def prime():
    '''
    Function returns the 10 001st prime number.
    '''
    prime_numbers = []
    num = 2
    while len(prime_numbers) != 10001:
        if sympy.isprime(num):
            prime_numbers.append(num)
        num += 1
    return prime_numbers[-1]


if __name__ == '__main__':
    print(prime())
