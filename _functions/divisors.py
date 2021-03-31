# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.
# >>>>>>>>>>>>>>>>>>>>>>
# WIP
# MAKE INTO FUNCTION

usr_num = int(input('enter a number for a list of its divisors, from 1-100. >> '))
divisors = list(range(1, 1000001))
b = []

# ----

for i in divisors :
    if usr_num % i == 0 :
        b.append(i)
    else :
        continue

# ----

print(b)

# ......................
