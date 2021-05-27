# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

# def chop(l) :
    # del(l[0])
    # del(l[-1])

# test_list = ['cats', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'f']
test_str = 'cats 1 2 3 4 5 6 7 8 9 10 f'
test_list = test_str.split()

# chop(test_list)
print(test_list)


# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle(l) :
    return test_list[:11]

x = middle(test_list)
print(x)
