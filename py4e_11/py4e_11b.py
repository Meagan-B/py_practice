# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
#
# >>>>>>>>>>>>>>
import re


file_inp = input('ENTER FILE NAME >>> ')
f_handl = open(file_inp)


num_collect = []
for line in f_handl :
    if re.search('[0-9]+', line) is not None:
        line = line.rstrip()
        line = line.split()
        for item in line :
            num_find = re.findall('[0-9]+', item)
            # print(num_find)
            if len(num_find) == 1 :
                num_collect.append(int(num_find))
            # elif len(num_find) > 1 :
            #     for item

# print(num_collect)
#
