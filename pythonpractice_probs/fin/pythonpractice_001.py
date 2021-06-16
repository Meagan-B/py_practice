#Create a program that asks the user to enter their name and their age. Print out a
#message addressed to them that tells them the year that they will turn 100 years old.
#Add on to the previous program by asking the user for another number and printing out that
#many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string
#"\n is the same as pressing the ENTER button)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
import datetime
current_date = datetime.datetime.utcnow()
#----••••••••----••••••••----••••••••----#
def time_to_100(p):
    if p == 'Y' or 'y' :
           
        usrname = input('enter your name >>')
        print('hello, ' + usrname.capitalize())
        
        usrage = input('enter your age >>')
        if isinstance(object, type) == False :
            print('!ERROR! enter age in numbers >>')
            return
        else :
            i_usrage = int(usrage)

        if i_usrage < 100 :
            yrscalc = 100 - i_usrage
            mscalc = yrscalc * 12
            wkscalc = yrscalc * 52
            dyscalc = 365 *  yrscalc
            num_dysto100 = current_date + datetime.timedelta(days = dyscalc)


        print('you will turn 100 in {0} years, in the year >>> {1}\nyou will turn 100 in {2} months\nyou will turn 100 in {3} weeks\nyou will turn 100 in {4} days'.format(yrscalc, num_dysto100.year, mscalc, wkscalc, num_dysto100))
        print('%s years to 100' % yrscalc)
        print('%s months to 100' % mscalc)
        print('%s weeks to 100' % wkscalc)
        print('%s days to 100' % dyscalc)
        return
    
    elif p == 'N' or 'n':
        return
#----••••••••----••••••••----••••••••----#             
play = input('would you like to play? (Y/N)\n>>> ')
time_to_100(play)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#