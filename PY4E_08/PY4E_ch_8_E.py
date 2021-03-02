# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the
# numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the
# max() and min() functions to compute the maximum and minimum numbers after the loop completes.
#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

usr_nums = list()
# creates empty list for loop below to fill

usr_inp = input('enter numbers (enter done, when finished) >>> ')
count = 0
while usr_inp is =< 0 or > 0 :
    print(usr_inp)
    if item in usr_nums : continue
    elif item in usr_nums == 'done': break
    else :
        usr_nums.append(usr_inp)
    count += 1
    

print(usr_nums)
