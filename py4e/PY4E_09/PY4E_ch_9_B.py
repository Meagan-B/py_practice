# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and keep a running count
# of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
#
# Sample Line:
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Sample Execution:
#
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}
#
#  >>>>>>>>>>>>>>>>>>>>>

usr_inp = input('enter file name >>> ')
fhandl = open(usr_inp)

prsd_lines = list()
count = 0
for line in fhandl:
    words = line.split()
    # print(words)
    # if len(words) < 1 or words == '' or words[0] != 'From':
    #     print('IGNORE', words)
    if len(words) < 1 or words == '' or words[0] != 'From': continue
    else :
        prsd_lines.append(words[2])
        count += 1
if count == 0 :
        print('NOT DETECTED')


d = dict()
for dotw in prsd_lines :
    d[dotw] = d.get(dotw,0) + 1
print(d)
