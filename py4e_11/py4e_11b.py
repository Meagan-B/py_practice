# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
#
# >>>>>>>>>>>>>>
# importing regular expression module
import re

# takes file name from user then opens and assigns to var f_handl
file_inp = input('ENTER FILE NAME >>> ')
f_handl = open(file_inp)

# creats empty list
num_collect = []
# FIRST for loop that looks at every line in opened user file living in var f_handl
for line in f_handl :
    # .rstrip() removes WHITESPACE at end of line in f_handl
    line = line.rstrip()
    # .split() splits the line into a list of items
    line = line.split()
    # SECOND for loop that looks at every element (item) in every line within f_handl
    for items in line :
        # searches each item for a match to the regex '\d+', looking for a digit of 1 or more characters in 'items', and assigns it to var num_find
        num_find = re.findall('\d+', items)
        # THIRD four loop that breaks apart the elements (i) in num_find , if there are more than one collected digit in the iteration it seperates elements (i) so they may be converted to a floating point
        for i in num_find :
            # if the length of element (i) is not equal to zero OR a value of None the following loop is executed
            if len(i) != 0 or len(i) is not None :
                # converts element(i) from num_find to float value
                num = float(i)
                # appends (adds to the end) value of num (assigned above)
                num_collect.append(num)
            # cut else loop in favor of second for loop to break apart items in num_find, as some lines had multiple digits to collect.

# prints the sum of the entire list (num_collect)
print('%s digits collected…' % len(num_collect))
print('…with a sum of %s' % sum(num_collect))
