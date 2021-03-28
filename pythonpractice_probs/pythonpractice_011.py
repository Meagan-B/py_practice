# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
#
# >>>>>>>>>>>>>>>>>>>>>

usr_n_str = input('\nenter a number below to see if it is a PRIME NUMBER……\n**** a prime number is a number with no divisors ****\n>>> ')

# ----

def prime_calc(n) :
    global usr_n_str
    end_ints = [2, 3, 4, 5, 6, 8, 9]

    usr_n = int(usr_n_str)
    last_dig = usr_n % 10

    for i in end_ints :
        if i == usr_n :
            return False

    if usr_n <= 1 :
        # print('exit 1')
        return False

    elif len(usr_n_str) > 1 :
        for i in end_ints :
            if last_dig == i :
                # print('exit 2')
                return False

    for n in range(2, usr_n) :
        if usr_n % n == 0 :
        # print('exit 3')
            return False
        else :
            # print('exit 4')
            return True

# ----

if prime_calc(usr_n_str) == False :
     print('\n{0} is NOT a prime number\n'.format(usr_n_str))
elif prime_calc(usr_n_str) == True :
     print('\n{0} IS a prime number\n'.format(usr_n_str))

# ...........................
