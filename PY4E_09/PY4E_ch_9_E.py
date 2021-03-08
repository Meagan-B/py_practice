# Exercise 5: This program records the domain name (instead of the address) where the message was sent from
# instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
#
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
#
#  >>>>>>>>>>>>>>>>>>>>>
import string


usr_fil = input('Enter a file name: ')
f_handl = open(usr_fil)


email_d = dict()
count = 0
for line in f_handl :
    if len(line) < 1 or line == ' ' or line[0] != 'From' : continue
    else :
        line = line.rstrip()
        line = translate(maketrans('.', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words :
            if word not in email_d:
                email_d[word] = 1
            else :
                email_d[word] += 1
        prsd_lines.append(words)
        print(prsd_lines)
        count += 1
# if count == 0 :
#         print('NOT DETECTED')
print(email_d)
