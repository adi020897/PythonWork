fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
count = dict()
fh = open(fname)

for line in fh:
    if not line.startswith("From") : continue
    if line.startswith("From:") : continue
    word = line.split()
    hr = word[5].split(':')
    count[hr[0]] = count.get(hr[0],0) + 1
    
for key,val in sorted(count.items()):
    print key,val
