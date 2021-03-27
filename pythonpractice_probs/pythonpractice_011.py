# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
#
# >>>>>>>>>>>>>>>>>>>>>

import re

# ----

usr_n = input('\nenter a number below to see if it is a PRIME NUMBER……\n**** a prime number is a number with no divisors ****\n>>> ')

# ----

print(len(usr_n))

if len(usr_n) > 1 and re.search('$[02345689]', usr_n)  :
    print('\n{0} is NOT a prime number\n'.format(n))
else :
    print('butts')




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
