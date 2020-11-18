# Prime permutations
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

import sympy


def check(number):
    '''
    Function checks if each of the three terms are prime, and each of the 4-digit numbers
    are permutations of one another.
    :param int number: prime number from start to end
    :return: number if the conditions are met, False - if not
    '''
    number2 = number + 3330
    number3 = number2 + 3330
    text1 = [i for i in str(number)]
    text2 = [i for i in str(number2)]
    text3 = [i for i in str(number3)]
    if len(text3) > 4:
        return False
    if sympy.isprime(number2) is False or sympy.isprime(number3) is False:
        return False
    for el in text1:
        if el in text2 and el in text3:
            pass
        else:
            return False
    return number


def search(start, end):
    '''
    The main function.
    :param int start: start range
    :param int end: end range
    :return: 12-digit number
    '''
    prime_numbers = list(sympy.primerange(start, end))
    possible_numbers = [el for el in prime_numbers if type(check(el)) is int]
    result = possible_numbers[1]
    return str(result) + str(result+3330) + str(result+6660)


if __name__ == '__main__':
    print(search(1000, 9999))
