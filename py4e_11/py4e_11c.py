# >>>>>>>>>>>>>>>>>>>
# Exercise 2: Write a program to look for lines of the form:
#
# New Revision: 39772
# >>>>>>>>>>>>>>>>>>>>

import re


print([str(i) for i in re.findall('New\s\w:\s\d+', open(input('ENTER FILE NAME >>> ')).read())])




# >>>>>>>>>>>>>>>>>>>
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.
#
# Enter file:mbox.txt
# 38549
#
# Enter file:mbox-short.txt
# 39756
# >>>>>>>>>>>>>>>>>>
