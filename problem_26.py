# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring 
# cycle in its decimal fraction part.


def convert(numerator, denominator):
    '''
    Function return recurring cycle in decimal fraction part of the fraction.
    :param int numerator: the dividend (number) that becomes the numerator
    :param int denominator: the divisor (number), which is called the denominator
    '''
    answear = ''
    l = {}
    index = 0
    numerator = numerator % denominator
    l[numerator] = index
    t = False
    while t == False:
        if numerator == 0:
            break
        digit = numerator * 10 // denominator
        numerator=numerator * 10 - (numerator * 10 // denominator) * denominator
        if numerator not in l:
            answear += str(digit)
            index += 1
            l[numerator] = index
            t = False
        else:
            answear += str(digit)
            t = True
    return answear


def find_max_cycle(number):
    '''
    Main function. Return the denominator of the fraction 
    with the longest recurring cycle in its decimal fraction part. 
    :param int number: the maximum possible of the denominator
    '''
    result = ''
    d = 1
    for i in range(1, number+1):
        cycle = convert(1, i)
        if len(result) < len(cycle):
            result = cycle
            d = i
    return d


print(find_max_cycle(1000))
