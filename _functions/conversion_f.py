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