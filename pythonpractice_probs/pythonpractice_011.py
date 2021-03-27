# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
#
# >>>>>>>>>>>>>>>>>>>>>


# ----

usr_n = int(input('enter a number for a list of its divisors, from 1-10. >> '))

# ----

def prime_calc(usr_n) :
    if usr_n  <= 1 :
        return False

    for i in range(2, usr_n) :
        if usr_n % i == 0 :
            return False
        else :
            return True
    print('end of function')
# ----

if prime_calc(usr_n) is False :
    print('\n%s is NOT a prime number' % usr_num)
elif prime_calc(usr_n) is True :
    print('\n%s IS a prime number' % usr_num)

# ----



# ----

# ----


# ...........................
