# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
welcome = '••••§•••• DIVISOR CHECKER ••••§••••\n'
print(welcome)
#----••••••••----••••••••----••••••••----#
def divisor_check(n) :
    for d in n :
        
    divisors = list(range(1, n))
    print(divisors)
    b = []

    for i in divisors :
        if n % i == 0 :
            b.append(i)
        else :
            continue

    print(b)
#----••••••••----••••••••----••••••••----#
div_inp = input('enter the number(s) you would like to check below,\n>>> ')
div_lst = div_inp.split()
div_int_lst = [int(i) for i in div_lst]
#print(div_inp, div_lst, div_int_lst)
#----••••••••----••••••••----••••••••----#
divisor_check(div_int_lst)
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
