# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
# >>>>>>>>>>>>>>>>>>>>>>>


import re

file_inp = input('ENTER FILE NAME >>> ')
f_handl = open(file_inp)

count = 0
usr_srch = input('SEARCH REGEX >>> ')
if usr_srch.endswith(' ') :
    usr_a = input('DID YOU MEAN TO END W WHITESPACE ??? (y for YES, n for NO) >>> ')
    if usr_a == 'y' :
        usr_str = str(usr_srch)
        for line in f_handl :
            if re.search(usr_str, line) :
                count += 1
                print(line)
    elif usr_a == 'n' :
        usr_str = str(usr_srch)
        usr_clean = usr_str.rstrip()
        for line in f_handl :
            if re.search(usr_clean, line) :
                count += 1
                print(line)
    else :
        print('BOO ERROR')


print('%s LINES MATCHING REGEX' % count)
