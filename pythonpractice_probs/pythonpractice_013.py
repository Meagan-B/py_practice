# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
#
# >>>>>>>>>>>>>>>>>>>>>


# ----

def Fibonnaci() :
    fib_lst = []
    lst_len = int(input('enter number for length of Fibonnaci below\n>>> '))

    count = 0

    while count == 0 :
        a = 1
        b = 1
        c = a + b
        fib_lst.append(c)
        count += 1
        a = c
        b = a

    while count > 0 and count < lst_len :
        # a = 1
        print('A: {0}'.format(a))
        # b = 1
        print('B: {0}'.format(b))
        c = a + b
        print('C: {0}'.format(c))
        fib_lst.append(c)
        count += 1
        print('COUNT: {0}'.format(count))
        a = c
        print('A2: {0}'.format(a))
        b = a
        print('B2: {0}'.format(b))

    # print(fib_lst)

    return

# ----

Fibonnaci()

# ...........................
