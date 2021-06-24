#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
welcome = '~~~~~ HOURLY RATE CALCULATOR ~~~~~\n••••••••••••••••••••••••••••••'
print(welcome)
#----••••••••----••••••••----••••••••----#
inp_hrs = input('hours for the week of {0}\n>>> '.format())
inp_rate = input('hourly rate\n>>> ')
y_or_n_overtime = input('do you recieve bonus pay for overtime?\n(Y/N) >>> ')
if y_or_n_overtime == 'Y' or 'y' :
    inp_overtime = input('overtime multiplier\n>>> ')
else :
    inp_overtime = None 
#----••••••••----••••••••----••••••••----# 
def hourly_rate(h, r, o) :
    
#----••••••••----#
    if h.isdigit() == True and r.isdigit() == True and inp_overtime == True :
        hrs = float(inp_hrs)
        rate = float(inp_rate)
        ot_multi = float(inp_overtime)
#----••••        
        if hrs > 40 :
            ot_rate = 
    
        print('HRS >>> {0}\nHOURLY RATE >>> {1}\nTOTAL PAY >>> {2} '.format(hrs, rate, (hrs * rate)))
#----••••••••----#      
    else :
        print('ERROR\n>>> accepts numbers only'.format())
#----••••••••----••••••••----••••••••----# 
hourly_rate(inp_hrs, inp_rate, inp_overtime)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#