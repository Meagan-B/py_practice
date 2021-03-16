# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

import re

file_inp = import('ENTER FILE NAME >>> ')
f_handl = open(file_inp)
usr_srch = import('SEARCH REGEX >>> ')

count = 0
for line in f_handl :
    line = line.rstrip()
    if re.search(usr_srch, line) :
        count += 1
        print(line)
print('%s LINES MATCHING REGEX' % count)
