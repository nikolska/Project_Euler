# Amicable numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


def check_sum_div(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    sum_ = 0
    for i in divisors:
        sum_ += i
    return sum_


def check_amicable(a, b):
    if check_sum_div(a) == b and check_sum_div(b) == a and a != b:
        return True


def main_func():
    amicable_list = []
    for i in range(1, 10001):
        sum_ = check_sum_div(i)
        if check_amicable(i, sum_):
            if i not in amicable_list:
                amicable_list.append(i)
    sum_ = 0
    for i in amicable_list:
        sum_ += i
    return sum_


print(main_func())
