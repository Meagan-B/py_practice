# Take two lists, say for example these two:
#
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
#
# Extra:
#
# Randomly generate two lists to test this
#
# >>>>>>>>>>>>>>>>>>>>>

import random

# ----

set_a = set(random.sample(range(1, 25), 5))
set_b = set(random.sample(range(1, 25), 5))

# ----

print('random set A = %s\n' % set_a)
print('random set B = %s\n' % set_b)

print('%s MATCHES found……' % len(set_a.intersection(set_b)), set_a.intersection(set_b))

# ----

rand_roll = 0

while len(set_a.intersection(set_b)) != 5 :
    set_a = set(random.sample(range(1, 25), 5))
    set_b = set(random.sample(range(1, 25), 5))
    rand_roll += 1

print('TOTAL set match found in %s iterations' % rand_roll)
print('matching sets = %s • %s' % (set_a, set_b))

# ----

# ...........................
