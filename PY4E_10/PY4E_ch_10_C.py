# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case
# and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter frequency varies between languages.
# #
# ------------------------------
import string
usr_file = input('FILE NAME >>>')
f_handl = open(usr_file)

d_lttrs = dict()
for line in f_handl :
    # print(line)
    line = line.rstrip()
    # print(line)
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    # print(line)
    words = line.split()
    # print(words)
    lttrs = list(str(words))
    # print(lttrs)
    for l in lttrs :
        if l == ' ' or l == "'" or l == None : continue
        d_lttrs[l] = d_lttrs.get(l, 0) + 1


print(d_lttrs)



    # lttrs = words.split
    # for lttrs in words :
    #
    #     print(lttrs)





# Sort the dictionary by value
