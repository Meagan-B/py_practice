# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order
# >>>>>>>>>>>>>>>>>>>>>

def flip_it_and_revrs_it() :

    usr_str = input('enter string below\n>>> ').strip()
    print(usr_str)

# ----

    usr_str = usr_str.split(' ')
    usr_str.reverse()

# ----

    rev_str = ''

    for i in usr_str :
        rev_str += i
        rev_str += ' '
# ----

    print(rev_str)

# ----

flip_it_and_revrs_it()

# ...........................
