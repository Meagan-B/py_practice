# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
#
# >>>>>>>>>>>>>>
import re


file_inp = input('ENTER FILE NAME >>> ')
f_handl = open(file_inp)


num_collect = []
for line in f_handl :
    # line = line.rstrip()
    if re.search('\s([0-9]+)', line) is not None :
        num_find = re.findall('\s([0-9]+)', line)
        if len(num_find) > 0 :
            print(num_find)
            # num_collect.append(int(num_find))

print(num_collect)
# 
