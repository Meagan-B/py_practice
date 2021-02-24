# write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and
# print out this new list.
#
# Write this in one line of Python.
#
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


a = [1, 3, 2, 4, 19, 23, 278, 10, 736, 0.5]
b = []

for num in a :
    if num < 5 :
        b.append(num)
        # print(b)
    else :
        continue
print(b)
b.sort()
print(b)
