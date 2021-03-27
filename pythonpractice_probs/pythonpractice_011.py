# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
#
# >>>>>>>>>>>>>>>>>>>>>


# ----

usr_num = int(input('enter a number for a list of its divisors, from 1-10. >> '))

# ----

nums = list(range(1, 10))
b = []

# ----

# for i in nums :
while usr_num > 1 :
    if usr_num % 2 == 0 :
        print('\n%s is NOT a prime number' % usr_num)
        usr_num = 0
        break
    elif usr_num % 3 == 0 : 
        print('\n%s is NOT a prime number' % usr_num)
        usr_num = 0
        break
    print('still in while loop')

# ----

# print(b)


# ----

# ----


# ----


# ...........................
