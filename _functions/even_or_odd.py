# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
# >>>>>>>>>>>>>>>>>

def even_or_odd() :

    num = input("enter a number below\n>>> ").rstrip()
    fl_num = float(num)

    if fl_num % 2 == 0 :
        print("{0} is even".format(fl_num))
    else :
        print("{0} is odd".format(fl_num))

#----

even_or_odd()

#................
