# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
#
# >>>>>>>>>>>>>>>>>>>>>

def check_pdrone() :

    usr_word = input('enter STRING below\n>>> ')
    usr_chars = list(usr_word.rstrip())
    lst_rv = usr_chars[::-1]

    if usr_chars == lst_rv :
        print('……{0} IS a palindrome'.format(usr_word))
    else :
        print('……{0} is NOT a palindrome'.format(usr_word))

# ----

check_pdrone()

# ...........................
