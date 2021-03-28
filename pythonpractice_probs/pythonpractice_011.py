# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
#
# >>>>>>>>>>>>>>>>>>>>>

import re

# ----

usr_n_str = input('\nenter a number below to see if it is a PRIME NUMBER……\n**** a prime number is a number with no divisors ****\n>>> ')
usr_n = int(usr_n_str)

# ----

ints = [2, 3, 4, 5, 6, 8, 9]
last_dig = usr_n % 10


if len(usr_n_str) > 1 :
    # print(type(last_dig))
    print(last_dig)
    for i in ints :
        if last_dig == i :
            # print('BOB1')
            print('\n{0} is NOT a prime number\n'.format(usr_n))
        else : continue

if usr_n <= 1 :
    # print('BOB2')
    print('\n{0} is NOT a prime number\n'.format(usr_n))

for n in range(2, usr_n) :
    if usr_n % n == 0 :
        # print('BOB3')
        print('\n{0} is NOT a prime number\n'.format(usr_n))
    else : continue

print('out of loop')


# ----

def prime_calc(n) :
    if len(usr_n) > 1 and re.search('$[02345689]', usr_n)  :
        print('\n{0} is NOT a prime number\n'.format(n))
        return False

    n = int(n)
    if n <= 1 :
        print('\n{0} is NOT a prime number\n'.format(n))
        return False

    for i in range(2, n) :
        if usr_n % i == 0 :
            print('\n{0} is NOT a prime number\n'.format(n))
            return False
        else :
            print('\n{0} IS a prime number\n'.format(n))
            return True
# ----

# prime_calc(usr_n)

# ...........................
