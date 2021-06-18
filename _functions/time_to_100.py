#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
def time_to_100(p):
    from datetime import date
    p = p.split()
#----••••••••----# 
    if p[0] == 'Y' or p[0] =='y' :
#----••••••••----#            
        usrname = input('enter your name >>')
        usrname = usrname.replace(' ', '')
        print('hello, ' + usrname.capitalize())
#----••••••••----#         
        usrage = input('enter your age >>')
        if isinstance(object, type) == False :
            print('!ERROR! enter age in numbers >>')
            return
        else :
            i_usrage = int(usrage)
#----••••••••----#           
        current_date = date.today()
        print("\ntoday's DATE >>> {0}\n".format(current_date))
#----••••••••----#         
        if i_usrage < 100 :
            yrscalc = 100 - i_usrage
            year_of_100 = current_date.year + yrscalc
            mscalc = yrscalc * 12
            wkscalc = yrscalc * 52
            dyscalc = 365 *  yrscalc
            
#----••••••••----# 
        print('{0} will turn 100 in {1} days, {2} weeks, {3} months and {4} years,\nin the year >>> {5}'.format(usrname, dyscalc, wkscalc, mscalc, yrscalc, year_of_100))
        return
#----••••••••----#     
    elif p[0] == 'N' or p[0] =='n':
        print('!!¡¡!!¡¡ •GAME OVER• ¡¡!!¡¡!!')
        return
#----••••••••----••••••••----••••••••----#             
play = input('would you like to play? (Y/N)\n>>> ')
time_to_100(play)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#