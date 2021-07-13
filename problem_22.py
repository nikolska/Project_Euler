# Names scores
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
# first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

from string import ascii_uppercase

file = open('names.txt', 'r')
list_ = [name for name in file]
list_names = list_[0].split(',')
sorted_names = sorted(list_names)

letters = [i for i in ascii_uppercase]
digits = range(1, 27)
dictionary = dict(zip(letters, digits))

main_points = 0
name_points = 0
n = 1
for name in sorted_names:
    for letter in name:
        if letter in dictionary:
            name_points += dictionary[letter]
    points = n * name_points
    main_points += points
    name_points = 0
    n += 1

print(main_points)

file.close()
