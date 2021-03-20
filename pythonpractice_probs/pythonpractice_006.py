# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
#
# >>>>>>>>>>>>>>>>>>>>>
# WIP

usr_word = input('enter STRING >>> ')
print('checking for palindromes……')


# def palind_fun(string) :
#     usr_chars = list(usr_word.rstrip())
#     if usr_chars[0] != usr_chars[-1] :
#         print('……%s is NOT a palindrome!' % usr_word)
#     elif usr_chars[0] == usr_chars[-1] :
#         chars_reverse = usr_chars.reverse()
#         if usr_chars == chars_reverse :
#             print('……%s is a palindrome!' % usr_word)
#     else :
#         print('OoPs!')
#
# palind_fun(usr_word)


usr_chars = list(usr_word.rstrip())
if usr_chars[0] != usr_chars[-1] :
    print('……%s is NOT a palindrome!' % usr_word)
elif usr_chars[0] == usr_chars[-1] :
    chars_reverse = usr_chars.reverse()
    if usr_chars == chars_reverse :
        print('……%s is a palindrome!' % usr_word)
else :
    print('OoPs!')
