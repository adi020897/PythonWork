fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
count = dict()
fh = open(fname)

for line in fh:
    if not line.startswith("From") : continue
    if line.startswith("From:") : continue
    word = line.split()
    count[word[1]] = count.get(word[1],0) + 1
         
maxkey = None
maxval = None
for key,val in count.items():
    if maxval is None or val>maxval:
        maxkey = key
        maxval = val

print maxkey,maxval
