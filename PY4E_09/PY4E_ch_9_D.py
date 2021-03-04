# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195
#
#  >>>>>>>>>>>>>>>>>>>>>


usr_inp = input('enter file name >>> ')
fhandl = open(usr_inp)

prsd_lines = list()
count = 0
for line in fhandl:
    l_splt = line.split()
    # print(words)
    # if len(words) < 1 or words == '' or words[0] != 'From':
    #     print('IGNORE', words)
    if len(l_splt) < 1 or l_splt == '' or l_splt[0] != 'From': continue
    else :
        prsd_lines.append(l_splt[1])
        count += 1
if count == 0 :
        print('NOT DETECTED')

# print(prsd_lines)

d = dict()
for words in prsd_lines :
    d[words] = d.get(words,0) + 1
# print(d)
#
# lst = list(d.values())
# lst.sort()
# print(lst)
for key in d :
    print(key, d[key])
for value in d :
    print(value, d[value])


# for val in d :
#     if val >
#
# counts[key]




# print(d.values())
# max_val = max(d.values())
# min_val = min(d.values())
# print(max_val, min_val)
# key_max = [ key for key in d if d[key] == max_val ]
# key_min = [ key for key in d if d[key] == min_val ]
# print(key_max, key_min)

# itm_max = key_max.append(max_val)
# itm_min = key_min.append(min_val)
# print('the MOST emails were sent by, %s' % itm_max)
# print('the LEAST emails were sent by, %s' % itm_min)

#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
### geeks for geeks
## Using min() + list comprehension + values()
## Finding min value keys in dictionary
# temp = min(test_dict.values())
# res = [key for key in test_dict if test_dict[key] == temp]
