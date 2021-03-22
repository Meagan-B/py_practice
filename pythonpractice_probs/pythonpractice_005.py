# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#
#>>>>>>>>>>>>>>>>>>>>>
import random

#----

print('SET MATCH, checks for element matches, does not count duplicates……')

#----
# comparison with a previously determined list

# lst_a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
# lst_b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
# set_a = set((lst_a))
# set_b = set((lst_b))
# print(type(set_a))
# c = set_a.intersection(set_b)
# print(set_a.intersection(set_b))

#----
# comparison with an imported user string, converted to list, via list()

# lst_a = list(input('enter items for set A >>> '))
# lst_b = list(input('enter items for set B >>> '))
# set_a = set((lst_a))
# set_b = set((lst_b))
# print(type(set_a))
# c = set_a.intersection(set_b)
# print(set_a.intersection(set_b))

#----

rand_a = []
while len(rand_a) <10 :
    val = random.randint(0,100)
    rand_a.append(val)


rand_b = []
while len(rand_b) <10 :
    val = random.randint(0,100)
    rand_b.append(val)

#----

set_a = set((rand_a))
set_b = set((rand_b))
print('set A : %s' % set_a, 'set B : %s' % set_b)

#----

c = set_a.intersection(set_b)
print('%s MATCHES found……' % len(c), c)

#----

print('end')

#........................
