# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the
# numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the
# max() and min() functions to compute the maximum and minimum numbers after the loop completes.
#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

usr_nums = list()

count = 0
while True :
    usr_inp = input('enter value to sort (when finished, enter done) >>> ')
    if usr_inp == 'done': break
    elif usr_inp == ' ' : continue
    try :
        f_usr_inp = float(usr_inp)
    except ValueError : continue
    else :
        usr_nums.append(f_usr_inp)
    count += 1

usr_min = min(usr_nums)
usr_max = max(usr_nums)
usr_sum = sum(usr_nums)

print('%s was your MINIMUM value ' % usr_min)
print('%s was your MAXIMUM value ' % usr_max)
print(count)
