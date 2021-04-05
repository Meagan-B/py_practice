# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
#
# >>>>>>>>>>>>>>>>>>>>>

def bookendz() :
    lst = input('enter a list of items below\nuse WHITESPACE (spacebar) to seperate list items\n>>> ').rstrip()
    lst = lst.split(' ')

    front = lst[0]
    back = lst[-1]
    
    print('the FIRST item of your list is…{0}\nthe LAST item of your list is…{1}'.format(front, back))

# ----

bookendz()

# ...........................
