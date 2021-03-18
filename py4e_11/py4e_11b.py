# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
#
# >>>>>>>>>>>>>>
import re


file_inp = input('ENTER FILE NAME >>> ')
f_handl = open(file_inp)


num_collect = []
for line in f_handl :
    line = line.rstrip()
    line = line.split()
    for items in line :
        num_find = re.findall('\d+', items)
        for i in num_find :
            if len(items) != 0 or len(items) is not None :
                num = float(i)
                num_collect.append(num)
        # elif len(num_find) > 1 :
        #     print('Len=2', num_find)
        #     num_splt = item.split()
        #     for i in num_splt :
        #         print(i)
                # num = float(i)
                # num_collect.append(num)


print(num_collect)
