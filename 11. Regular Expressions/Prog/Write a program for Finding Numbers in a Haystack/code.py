import re

fh = open('regex_sum_365473.txt')
no = list()
total = 0

for line in fh:
    tempno = re.findall('[0-9]+', line)
    no = no + tempno

for number in no:
    total = total + int(number)

print "The sum of all the integers in the file is", total
