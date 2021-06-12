# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
welcome = '••••§•••• DIVISOR CHECKER ••••§••••\n'
print(welcome)
#----••••••••----••••••••----••••••••----#
def divisor_check(n) :

    divisors = list(range(2, n))
    #print('divisors >>> {0}'.format(divisors))
    
    b = []

    for i in divisors :
        if n % i == 0 :
            b.append(i)
        else :
            continue
        
    if len(b) < 1 :
        if n == 0 or n == 1 :
            b = [n]
        else :
            b = [1, n]
           
    print('divisors for {0} >>> {1}'.format(n, b))
    return b
#----••••••••----••••••••----••••••••----#
div_inp = input('enter the number(s) you would like to check below,\n>>> ')
#print('div_inp >>> {0}'.format(div_inp)) 
div_lst = div_inp.split()
#print('div_lst >>> {0}'.format(div_lst))
div_int = [ int(d) for d in div_lst]
#print('div_lst >>> {0}'.format(div_int))
#----••••••••----••••••••----••••••••----#
x = [ int(d) for d in div_lst]
#----••••••••----••••••••----••••••••----#
for num in x :
    #print(num, type(num))
    divisor_check(num)
    
    if len(x) > 1 :
        
        
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
