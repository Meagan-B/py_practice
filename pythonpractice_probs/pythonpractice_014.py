# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
# >>>>>>>>>>>>>>>>>>>>>

usr_lst = input('enter list items below\n>>> ').split(' ')
print(usr_lst)

# ----

def dup_cut_1() :
    global usr_lst

    for i in usr_lst :
        if i in new_lst : continue
        elif i not in new_lst :
            new_lst.append(i)
            
    print(type(usr_lst))
    print(usr_lst)


# ----
# ----

def dup_cut_2() :
    global usr_lst

    usr_lst = set(usr_lst)
    usr_lst = list(usr_lst)

    print(type(usr_lst))
    print(usr_lst)

# ----
# ----



# ...........................
