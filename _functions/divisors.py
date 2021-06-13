# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
welcome = '••••§•••• DIVISOR CHECKER ••••§••••\n'
print(welcome)
#----••••••••----••••••••----••••••••----#
def divisor_check(n) :
    divisors = list(range(2, n))

    b = []

    for i in divisors :
        if n % i == 0 :
            b.append(i)
        
    if len(b) < 1 :
        if n == 0 or n == 1 :
            b = [n]
        else :
            b = [1, n]
    
    return b
#----••••••••----••••••••----••••••••----#
div_inp = input('enter the number(s) you would like to check below,\n>>> ')
div_lst = div_inp.split()
div_int = [ int(d) for d in div_lst]
#----••••••••----••••••••----••••••••----#   
def divisor_set_compare(x) :
    c = []
    
    for i in x :
        c += divisor_check(i)
        
    c =set(c)
    
    print('\ncommon DIVISOR(S) of {0} >>> {1}'.format(x, c))
#----••••••••----••••••••----••••••••----#        
for num in div_int :
    print('DIVISOR(S) for {0} >>> {1}'.format(num, divisor_check(num)))
    
if len(div_int) > 1 :
    divisor_set_compare(div_int)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
