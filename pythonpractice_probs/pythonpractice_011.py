# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
#
# >>>>>>>>>>>>>>>>>>>>>

import re

# ----

# usr_n = int(input('\nenter a number below to see if it is a PRIME NUMBER……\n**** a prime number is a number with no divisors ****\n>>> '))

# ----

def prime_calc(n) :
    # usr_n = int(input('\nenter a number below to see if it is a PRIME NUMBER……\n**** a prime number is a number with no divisors ****\n>>> '))
    if re.search('$[02345689]') :
        print('\n%s is NOT a prime number\n' % n)
        return False

    if n  <= 1 :
        print('\n%s is NOT a prime number\n' % n)
        return False

    for i in range(2, n) :
        if usr_n % i == 0 :
            print('\n%s is NOT a prime number\n' % n)
            return False
        else :
            print('\n%s IS a prime number\n' % n)
            return True
# ----

usr_n = int(input('\nenter a number below to see if it is a PRIME NUMBER……\n**** a prime number is a number with no divisors ****\n>>> '))

prime_calc(usr_n)

# if prime_calc(usr_n) is False :
#     print('\n%s is NOT a prime number\n' % usr_n)
# elif prime_calc(usr_n) is True :
#     print('\n%s IS a prime number\n' % usr_n)

# ...........................
