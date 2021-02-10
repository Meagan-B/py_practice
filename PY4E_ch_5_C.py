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

while num in usr_inp != 'DONE' or 'done' :
    try:
        usr_inp = int(input('enter a number, when you are done enter DONE:'))
    except:
        print('invalid input, enter a NUMBER')

    if num in usr_inp == 'DONE' or "done" :
        count = 0
        for num in [usr_inp]:
            count = count + 1
        print('COUNT: ', count)
        total = 0
        for num in [usr_inp]:
            total = total + num
        print('TOTAL: ', total)
        print('AVG: ', total/count)
print('END')
