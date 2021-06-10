# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
welcome = '••••§•••• DIVISOR CHECKER ••••§••••\n'
print(welcome)
#----••••••••----••••••••----••••••••----#
def divisor_check(n) :
    #print('n >>> {0}'.format(n))
    
    n_form = [ int(d) for d in n]
    #print('n_form >>> {0}'.format(n_form))    
    
    for e in n_form :
        divisors = list(range(1, e))
        #print('divisors >>> {0}'.format(divisors))
    
        b = []

        for i in divisors :
            if e % i == 0 :
                b.append(i)
            else :
                continue
            
        print('divisors for {0} >>> {1}'.format(e, b))
#----••••••••----••••••••----••••••••----#
div_inp = input('enter the number(s) you would like to check below,\n>>> ')
#print('div_inp >>> {0}'.format(div_inp)) 
div_lst = div_inp.split()
#print('div_lst >>> {0}'.format(div_lst)) 
#----••••••••----••••••••----••••••••----#
divisor_check(div_lst)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
