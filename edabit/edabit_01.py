age = input('enter age below\n>>> ')
age = int(age)

def calc_age(age):

	age_days = age * 365
	print('your age in years: {0}\nyour age in days: {1}'.format(age, age_days))

calc_age(age)
