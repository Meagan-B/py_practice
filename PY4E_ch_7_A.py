# Exercise 1: Write a program to read through a file and print the contents of the file (line by line)
# all in upper case. Executing the program will look as follows:
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500

def name_fun() :
    if file_name.endswith ('.txt') :
        return file_name
    raise ValueError('extension must be .txt')

file_name = input ('Enter a file name: ')
ver_file_name = f_name_fun(file_name)

openread = open(file_name, 'r')
lines_mbox = openread.readlines()

count = 0
for line in lines_mbox :
    count += 1
    print('Line %s : %s /n' % (count, lines_mbox.uppercase))
    print(end)
