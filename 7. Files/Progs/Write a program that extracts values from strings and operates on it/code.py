# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
fstr=0.0
avg=0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    str = line[pos+1:]
    fstr = fstr + float(str)
    count = count + 1
avg = fstr/count
print "Average spam confidence:",avg