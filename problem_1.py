# Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def multiples():
    '''
    Function makes list of all the multiples of 3 or 5 below 1000.
    :return: sum of the digits
    '''
    list_num = [i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0]
    return sum(list_num)


if __name__ == '__main__':
    print(multiples())
