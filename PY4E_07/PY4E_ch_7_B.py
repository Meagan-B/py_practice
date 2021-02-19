# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file,
# print out the average spam confidence.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.


#WIP

def name_fun(file_name) :
    if file_name.endswith('.txt') :
        return file_name
    if not file_name.endswith('.txt') :
        raise ValueError('extension must be .txt')
        # exit()

file_name = input('Enter a file name: ')
ver_file_name = name_fun(file_name)
fhandle = open(ver_file_name)
read_fhandle = fhandle.read()


print(fhandle)


spam_count = 0
spam_total = 0.000000000000
#      line_clean = line.rstrip()
for line in read_fhandle :
    if 'X-DSPAM-Confidence:' in line :
        spam_val = read_fhandle.split(':')
        print(spam_val)
        spam_count += 1
        print(spam_count, ')', spam_val)
    # try :
    #     float_val = float(spam_val)
    # except :
    #     print('pos, could not convert float from line')
#
# spam_total = spam_total + float_val
#     print('TOTAL: ', spam_total)



# spam_avg = spam_total / spam_count
# print('Average spam confidence: %s' % spam_avg)
