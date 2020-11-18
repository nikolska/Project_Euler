# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def multiple():
    '''
    Function iterates over all numbers starting from 2520, which are divisible by numbers from 1 to 20
    and stops when when it finds the first one.
    :return: the smallest number that is divisible by numbers from 1 to 20
    '''
    start = 2520
    condition = False
    while condition is False:
        for el in range(1, 21):
            if start % el == 0:
                condition = True
                continue
            else:
                condition = False
                break
        start += 10
    return start - 10


if __name__ == '__main__':
    print(multiple())
