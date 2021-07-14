# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations


def find_permutation(str_numbers):
    '''
    Function generates list of lexicographic permutations and return the millionth one.
    :param str str_numbers: string of numbers
    '''
    permutation = list(permutations(str_numbers))
    result = ''.join(permutation[999999])
    return result


print(find_permutation('0123456789'))
