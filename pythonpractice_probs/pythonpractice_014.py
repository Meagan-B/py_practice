# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
# >>>>>>>>>>>>>>>>>>>>>

usr_lst = input('enter list items below\n>>> ').split(' ')
# print(usr_lst)

# ----

def dup_cut_1() :
    global usr_lst
    org_len = len(usr_lst)
    new_lst = []

    for i in usr_lst :
        if i in new_lst : continue
        elif i not in new_lst :
            new_lst.append(i)

    new_len = len(new_lst)
    len_diff = org_len - new_len

    print('dup_cut_1 found {0} duplicates'.format(len_diff))
    # print(type(new_lst))
    print('ORIGINAL list\n{0}\nNEW list\n{1}'.format(usr_lst, new_lst))

# ----

def dup_cut_2() :
    global usr_lst
    org_len = len(usr_lst)

    new_lst = set(usr_lst)
    new_lst = list(new_lst)

    new_len = len(new_lst)
    len_diff = org_len - new_len

    print('dup_cut_2 found {0} duplicates'.format(len_diff))
    # print(type(usr_lst))
    print('ORIGINAL list\n{0}\nNEW list\n{1}'.format(usr_lst, new_lst))

# ----

dup_cut_1()
dup_cut_2()

# ...........................
