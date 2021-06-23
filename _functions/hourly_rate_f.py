#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
welcome = '~~~~~ HOURLY RATE CALCULATOR ~~~~~\n••••••••••••••••••••••••••••••'
print(welcome)
#----••••••••----••••••••----••••••••----#
inp_hrs = input('hours\n>>> ')
inp_rate = input('hourly rate\n>>> ')
inp_currency = input('currency of pay (default is USD)\n>>> ')
#----••••••••----••••••••----••••••••----# 
def hourly_rate(h, r, c) :
    
#----••••••••----#      
    if isdigit(hrs) and isdigit(rate) is True :
        hrs = float(inp_hrs)
        rate = float(inp_rate)
    
        print('HRS >>> {0}\nnHOURLY RATE >>> {1}\nTOTAL PAY >>> {2} '.format(hrs, rate, (hrs * rate)))
#----••••••••----#      
    else :
        print('ERROR\n>>> accepts numbers only'.format())
#----••••••••----#          
    from forex_python.converter import CurrencyRates
    
    cur_rates = CurrencyRates()
    
    cur_rates_dict = dict(cur_rates.get_rates('USD'))
    print(cur_rates_dict)
    
    inp_conversion = cur_rates_dict.get(c)
    print(inp_conversion)
    inp_conversion= upper(str(inp_conversion))
    print(inp_conversion)
#----••••••••----#
#from forex_python.bitcoin import BtcConverter
#b = BtcConverter()   # add "force_decimal=True" parmeter to get Decimal rates
#b.get_latest_price('EUR')   # you can directly call get_latest_price('EUR')

#----••••••••----••••••••----••••••••----# 
#hourly_rate(inp_hrs, inp_rate, inp_currency)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#