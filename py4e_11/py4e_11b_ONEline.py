# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
#
# >>>>>>>>>>>>>>
# importing regular expression module
import re

# one line challenge:
# print(); prints the format string '...with a sum of %s' (%s is a placeholder for what follows % outside of ''), here %s contains the sum of what lives within sum()
## within sum(); [] contain what will be summed, element(i) converted to integer via int(),
### followed by for loop to search each element (i) for match of following regex
#### re.findall(); contains our search parameters, '\d+' one or more digits, followed by what we are searching,
##### here we search a file given to us by the user via input(), which is then opened via open() and read via .read()
###### LASTLY; we must close all of our open () and []
print('sum of digits collected………%s' % sum([int(i) for i in re.findall('\d+', open(input('ENTER FILE NAME >>> ')).read())]))
