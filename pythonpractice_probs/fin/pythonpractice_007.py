# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
# 
# >>>>>>>>>>>>>>>>>>>>>

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# ----
# variable a_even is equal to the argument within [], create an an item(i) from item(i) in list(a) ONLY IF item(i) divided by 2 has a remainder(%) of 0,
a_even = [i for i in a if i % 2 == 0]
print(a_even)

# ...........................
