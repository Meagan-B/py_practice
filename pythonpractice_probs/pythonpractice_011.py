# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
#
# >>>>>>>>>>>>>>>>>>>>>
# WIP
usr_n_str = input('\nenter a number below to see if it is a PRIME NUMBER……\n**** a prime number is a number with no divisors ****\n>>> ')

# ----

def prime_calc(n) :
    global usr_n_str
    end_ints = [2, 3, 4, 5, 6, 8, 9]
    # usr_fl = float(usr_n_str)
    usr_i = int(usr_n_str)

    if usr_i == 2 :
        print('exit 1')
        return True

    if usr_i < 1 :
        # print('exit 2')
        print('{0} is less than 1'.format(usr_i))
        return False

    elif len(usr_n_str) > 1 :
        print(usr_n_str)
        last_dig = usr_i % 10
        for i in end_ints :
            if last_dig == i :
                # print('exit 3')
                print('{0} divided by {1} is {2}, with a remainder of 0…'.format(usr_i, i, (usr_i//i)))
                return False

    for n in range(2, usr_i) :
        # print(n)
        usr_n_chk = usr_i % n
        print(usr_n_chk, n)
    if usr_n_chk == 0 :
    # print('exit 4')
        print('{0} divided by {1} is {2}, with a remainder of 0…'.format(usr_i, n, (usr_i/n)))
        return False
    else :
        print('{0} divided by {1} is {2}, with a remainder of {3}…'.format(usr_i, n, (usr_i / n), float(usr_i % n)))
        print('exit 5')
        return True

# ----

if prime_calc(usr_n_str) == False :
     print('\n{0} is NOT a prime number\n'.format(usr_n_str))
elif prime_calc(usr_n_str) == True :
     print('\n{0} IS a prime number\n'.format(usr_n_str))

# ...........................
