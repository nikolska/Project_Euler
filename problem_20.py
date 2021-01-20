# Factorial digit sum
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

def fact(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    str_result = str(result)
    sum_ = 0
    for i in str_result:
        sum_ += int(i)
    return sum_


print(fact(100))
