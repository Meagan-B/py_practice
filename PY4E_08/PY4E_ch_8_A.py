# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.



def chop(l) :
    del(l[0])
    del(l[-1])

test_val = '*burp* hello, my name is computer, what lovely weather we are having today! eh?'
test_list = list(test_val)

chop(test_list)

print(test_list)








# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
