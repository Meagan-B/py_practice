# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
welcome = '••••§•••• DIVISOR CHECKER ••••§••••\n'
print(welcome)
#----••••••••----••••••••----••••••••----#
div_inp = input('enter the number(s) you would like to check below,\n>>> ')
div_lst = div_inp.split()
div_int = [ int(d) for d in div_lst]
div_set = set(div_int)
#----••••••••----••••••••----••••••••----#
print('\r')
#----••••••••----••••••••----••••••••----# 
def divisor_check(n) :
    divisors = list(range(2, n+1))

    b = []
    for i in divisors :
        if n % i == 0 :
            b.append(i)
    
    return b
#----••••••••----••••••••----••••••••----#  
def divisor_set_compare(x) :
    #from collections import Counter

    divisors = []
    for i in x :
        divisors += divisor_check(i)
    #print(divisors)
    
    freq = {}
    for n in divisors:
        if (n in freq):
            freq[n] += 1
        else:
            freq[n] = 1    
    #print('freq >>> {0}'.format(freq))      
  
    d = []
    for k, v in freq.items():
        if v == len(x) :
            d.append(k)
            #print ("{0} : {1}".format(k, v))
    
    return d
#----••••••••----••••••••----••••••••----#        
for num in div_set :
    div_results = divisor_check(num)
    if len(div_results) == 0 :
        print('{0} has no DIVISOR(s)'.format(num))
    else :    
        print('DIVISOR(s) for {0} >>> {1}'.format(num, div_results))
    
if len(div_set) > 1 :
    compare_results = divisor_set_compare(div_set)
    if len(compare_results) == 0 :
        print('\nno COMMON DIVISOR(s) between'.format(div_set))
    else :    
        print('\nCOMMON DIVISOR(s) for {0} >>> {1}'.format(div_set, compare_results))
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
