# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def find_sum(power):
    '''
    Function returns the sum of numbers that can be written 
    as the sum of fifth powers of their digits.
    :param int power: the power of digit
    '''
    numders_sum = 0
    for i in range(2, power * 9**power + 1): #5*9^5
        degrees = [int(i)**power for i in str(i)]
        if sum(degrees) == i:
            numders_sum += sum(degrees)
    return numders_sum


print(find_sum(5))
