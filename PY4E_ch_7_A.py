# Exercise 1: Write a program to read through a file and print the contents of the file (line by line)
# all in upper case. Executing the program will look as follows:
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500

#WIP
def name_fun(file_name) :
    if file_name.endswith('.txt') :
        return file_name
    raise ValueError('extension must be .txt')

file_name = input('Enter a file name: ')
#file_name = 'mboxshort.txt'
ver_file_name = name_fun(file_name)

# openedfile = open(file_name)
openedfile = open(ver_file_name)
readfile = openedfile.readlines()

count = 0
for line in readfile :
    count += 1
    print('Line %s : %s /n' % (count, readfile.toUpperCase()))

print(end)
