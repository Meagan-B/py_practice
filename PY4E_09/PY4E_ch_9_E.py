# Exercise 5: This program records the domain name (instead of the address) where the message was sent from
# instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
#
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
#
#  >>>>>>>>>>>>>>>>>>>>>

usr_fil = input('Enter a file name: ')
f_handl = open(usr_fil)


prsd_lines = list()
count = 0
for line in f_handl :
    l_splt = line.split()
    if len(l_splt) < 1 or l_splt == ' ' or l_splt[0] != 'From' : continue
    else :
        prsd_lines.append(line)
        print(prsd_lines)
        count += 1
if count == 0 :
        print('NOT DETECTED')


email_d = dict()
for words in prsd_lines :
    email_d[words] = email.d(words, 0) + 1
print(email_d)    
