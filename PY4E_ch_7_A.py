# Exercise 1: Write a program to read through a file and print the contents of the file (line by line)
# all in upper case. Executing the program will look as follows:
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500

#WIP
# def name_fun() :
#     if file_name.endswith('.txt' or '.pdf') :
#         return file_name
    #raise ValueError('extension must be .txt or .pdf')

file_name = input ('Enter a file name: ')
#ver_file_name = name_fun(file_name)

opened = open(file_name, 'r')
#opened = open(ver_file_name, 'r')
lines_file = opened.readlines()

count = 0
for line in lines_file :
    count += 1
    print('Line %s : %s /n' % (count, lines_file.uppercase))

print(end)
