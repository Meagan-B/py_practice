# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
#
# >>>>>>>>>>>>>>>>>>>>>

def Fibonnaci() :
    fib_lst = [1, 1]
    lst_len = int(input('enter number for length of Fibonnaci below\n>>> '))

    count = 2

    while count == 2 :
        a = 1
        b = 1
        c = a + b
        fib_lst.append(c)
        count += 1
        b = a
        a = c

    while count > 2 and count < lst_len :
        c = a + b
        fib_lst.append(c)
        count += 1
        b = a
        a = c
        print('A: {0}'.format(a))
        print('B: {0}'.format(b))
        print('C: {0}'.format(c))
        print('COUNT: {0}'.format(count))
        print('A2: {0}'.format(a))
        print('B2: {0}'.format(b))

    print(fib_lst)

    return

# ----

Fibonnaci()

# ...........................
