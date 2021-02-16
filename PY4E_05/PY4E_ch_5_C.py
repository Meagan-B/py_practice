#Exercise 2: Write another program that prompts for a list of numbers as
#above and at the end prints out both the maximum and minimum of the numbers
#instead of the average.

max = None
min = None
while True :
    usr_val = input('enter a number >')
    if usr_val == 'done' or usr_val == 'DONE':
        break
    try :
        f_usr_val = float(usr_val)
    except:
        print('invalid input')
        continue
    for num in [f_usr_val] :
        if min is None :
            min = num
        elif num < min :
            min = num
    for num in [f_usr_val] :
        if max is None :
            max = num
        elif num > max :
            max = num

print('Maximum is', max)
print('Minimum is', min)
