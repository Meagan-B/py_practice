#Exercise 1: Write a program which repeatedly reads numbers until the user
#enters “done”. Once “done” is entered, print out the total, count, and
#average of the numbers. If the user enters anything other than a number,
#detect their mistake using try and except and print an error message and
#skip to the next number.
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>
# count variable will hold value of number of items collected, total variable will hold value of the sum of all numbers in user input filled list,
count = 0
total = 0.0

#----
#
print('WELCOME, please enter numbers only & when you are done enter "done"')
while True :
    usr_val = input('enter a number >')
    if usr_val == 'done' or usr_val == 'DONE':
        break
    try :
        float_usr_val = float(usr_val)
    except:
        print('invalid input, enter a NUMBER')
        continue
    print(float_usr_val)
    count = count + 1
    total = total + float_usr_val

#----

print('COUNT:',count , '• TOTAL:',total , '• AVG:',total/count)
print('END')

#......................
