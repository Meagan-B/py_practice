# Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
#
#  >>>>>>>>>>>>>>>>>>>>>

usr_inp = input('enter file name >>> ')
fhandl = open(usr_inp)

d = dict()

for word in fhandl :
    d[word] = d.get(word,0) + 1
print(d)




# for word in fhandl :
#     items = lines.split()
#     # splits the sting of words in fhandle into list items
#     for item in items :
#         if item in words_dic : continue
#         # passes words already collected in our list ss_uniq_wrds
#         else :
#             words_dic.append(item)
#             # adds new words to our list
# print(words_dic)
