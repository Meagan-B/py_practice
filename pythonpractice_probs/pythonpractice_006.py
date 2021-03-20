# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
#
# >>>>>>>>>>>>>>>>>>>>>
# WIP

usr_word = input('enter STRING >>> ')
print('checking for palindromes……')


def reverse_fun(chars_reverse) :
    chars_reverse = list(usr_word.rstrip())
    chars_reverse.reverse()
    return chars_reverse

def palind_fun(usr_word) :
    usr_chars = list(usr_word.rstrip())
    if usr_chars[0] != [-1] :
        return (usr_word, 'is NOT a palindrome!')
    if usr_chars == chars_reverse :
        return (usr_word, 'is a palindrome!')

reverse_fun(usr_chars)
palind_fun(usr_word)
