#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
welcome = '~~~~~ HOURLY RATE CALCULATOR ~~~~~\n••••••••••••••••••••••••••••••'
print(welcome)
#----••••••••----••••••••----••••••••----#
inp_hrs = input('hours\n>>> ')
inp_rate = input('hourly rate\n>>> ')
#----••••••••----••••••••----••••••••----# 
def hourly_rate(h, r) :
    
#----••••••••----#
    if h.isdigit() == True and r.isdigit() == True :
        hrs = float(inp_hrs)
        rate = float(inp_rate)
    
        print('HRS >>> {0}\nHOURLY RATE >>> {1}\nTOTAL PAY >>> {2} '.format(hrs, rate, (hrs * rate)))
#----••••••••----#      
    else :
        print('ERROR\n>>> accepts numbers only'.format())
#----••••••••----••••••••----••••••••----# 
hourly_rate(inp_hrs, inp_rate)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#