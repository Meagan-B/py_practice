#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
welcome = '~~~~~ HOURLY RATE CALCULATOR ~~~~~\n••••••••••••••••••••••••••••••'
print(welcome)
#----••••••••----••••••••----••••••••----#
from datetime import date
inp_hrs = input('hours for the week of {0}\n>>> '.format(date.today()))
#----••••••••----••••••••----••••••••----# 
inp_rate = input('hourly rate\n>>> ')
#----••••••••----••••••••----••••••••----# 
y_or_n_overtime = input('do you recieve bonus pay for overtime?\n(Y/N) >>> ')
if y_or_n_overtime[0] == 'Y' or y_or_n_overtime[0] == 'y' :
    inp_overtime = input('overtime multiplier\n>>> ')
else :
    inp_overtime = None 
#----••••••••----••••••••----••••••••----# 
def hourly_rate(h, r, o) :
    if h.isdigit() == True and r.isdigit() == True:
        hrs = float(inp_hrs)
        rate = float(inp_rate)
#----••••        
        if hrs > 40 and inp_overtime is not None:
            ot_multi = float(inp_overtime)
            ot_pay = (hrs - 40) * (rate * ot_multi) 
            print('HRS >>> {0}\nHOURLY RATE >>> {1}\nTOTAL PAY >>> {2} '.format(hrs, rate, ((hrs * rate) + ot_pay)))
        else :
            print('HRS >>> {0}\nHOURLY RATE >>> {1}\nTOTAL PAY >>> {2} '.format(hrs, rate, (hrs * rate)))
#----••••••••----   
    else :
        print('ERROR\n>>> accepts numbers only'.format())
#----••••••••----••••••••----••••••••----# 
hourly_rate(inp_hrs, inp_rate, inp_overtime)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#