# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
#
# >>>>>>>>>>>>>>>>>>>>>

usr_word = input('enter STRING >>> ')
print('checking for palindromes……')

# ----

usr_chars = list(usr_word.rstrip())
lst_rv = usr_chars[::-1]

# ----

if usr_chars == lst_rv :
    print('……%s is a palindrome!' % usr_word)
else :
    print('……better luck next time :(')

# ----

# def check_pdrone() :
#     if usr_chars == lst_rv :
#         print('……%s is a palindrome!' % usr_word)
#     else :
#         print('……better luck next time :(')
#
# check_pdrone()

# ...........................
