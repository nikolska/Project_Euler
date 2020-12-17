# Self powers
#
# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
#
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

def powers(num):
    list_n = []
    for i in range(1, num + 1):
        list_n.append(i ** i)
    return sum(list_n)


number = powers(1000)
result = number % 10000000000
print(result)
