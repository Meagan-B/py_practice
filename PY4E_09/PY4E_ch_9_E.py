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


usr_inp = input('enter file name >>> ')
f_handl = open(usr_inp)


d = dict()
for line in f_handl:
    if line.startswith('From:') :
        # print(line)
        l_splt = line.split()
        # print(l_splt[1])
        e_addr = l_splt[1]
        uname, domain = e_addr.split('@')
        # print(domain)
        d[domain] = d.get(domain, 0) + 1


# print(d.keys())
# print(d.values())
# print(d.items())
print(sorted([(v, k) for k, v in d.items()], reverse=True))

#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
### copypaste of code from PY4E_ch_9_D
