# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many
# messages have come from each email address, and print the dictionary.
#
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}
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
        prsd_lines.append(words[1])
        count += 1
if count == 0 :
        print('NOT DETECTED')

# print(prsd_lines)

d = dict()
for dotw in prsd_lines :
    d[dotw] = d.get(dotw,0) + 1
print(d)
