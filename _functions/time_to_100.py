#Create a program that asks the user to enter their name and their age. Print out a
#message addressed to them that tells them the year that they will turn 100 years old.
#Add on to the previous program by asking the user for another number and printing out that
#many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string
#"\n is the same as pressing the ENTER button)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
import datetime
#----••••••••----••••••••----••••••••----#
def time_to_100(p):
    p = p.split()

    if p[0] == 'Y' or p[0] =='y' :
           
        usrname = input('enter your name >>')
        usrname = usrname.replace(' ', '')
        print('hello, ' + usrname.capitalize())
        
        usrage = input('enter your age >>')
        if isinstance(object, type) == False :
            print('!ERROR! enter age in numbers >>')
            return
        else :
            i_usrage = int(usrage)
          
        current_date = datetime.datetime.today()
        print(current_date)
        
        if i_usrage < 100 :
            yrscalc = 100 - i_usrage
            mscalc = yrscalc * 12
            wkscalc = yrscalc * 52
            dyscalc = 365 *  yrscalc
            year_of_100 = current_date
            

        print('you will turn 100 in {0} days, {1} weeks, {2} months and {3} years,\nin the year >>> {4}'.format(dyscalc, wkscalc, mscalc, yrscalc, year_of_100))
        return
    
    elif p[0] == 'N' or p[0] =='n':
        print('!!¡¡!!¡¡ •GAME OVER• ¡¡!!¡¡!!')
        return
#----••••••••----••••••••----••••••••----#             
play = input('would you like to play? (Y/N)\n>>> ')
time_to_100(play)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#