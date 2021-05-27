# Exercise 2: Write a program to look for lines of the form:
#
# New Revision: 39772
# >>>>>>>>>>>>>>>>>>>>


import re

usr_file = input('ENTER FILE NAME >>> ')
f_handl = open(usr_file)
r_file = f_handl.read()


lst_collect = []
# num_find = re.findall('\<New\> \<Revision\>: \d+', f_handl)
# lst_collect.append(num_find)

for line in r_file :
    line = line.rstrip()
    line_find = re.search('New.+: \d+', line)
    ## usr_srch = input('SEARCH REGEX >>> ')
    ## usr_srch = re.search(usr_srch, line)
    ## usr_srch = re.search(input('SEARCH REGEX >>> '), line)
    ## lst_collect.append(usr_srch)
    ### print(num_find = re.search('New\s\w:\s\39772', line)
    lst_collect.append(line_find)

print(lst_collect)

# >>>>>>>>>>>>>>>>>>>
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.
#
# Enter file:mbox.txt
# 38549
#
# Enter file:mbox-short.txt
# 39756
# >>>>>>>>>>>>>>>>>>
