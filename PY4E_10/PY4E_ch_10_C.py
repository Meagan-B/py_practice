# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case
# and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter frequency varies between languages.
# #
# ------------------------------
import string
usr_file = input('FILE NAME >>>')
f_handl = opent(usr_file)


for line in fhandl :
    print(line)
    line = line.rstrip()
    print(line)
    line = line.translate(str.maketrans(' ' , string.punctuation))
    line = line.lower()
    print(line)
    words = line.split()
    print(words)
    lttrs = words.split
    print(lttrs)

# make dictionary of letters (lttrs)

# d_lttrs = dict()


# Sort the dictionary by value
