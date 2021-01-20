# Power digit sum

# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2**1000?

def power_sum(power):
    digit = str(2**power)
    sum_ = 0
    for i in digit:
        sum_ += int(i)
    return sum_


print(power_sum(1000))
