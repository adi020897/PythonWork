count = dict()
line = raw_input("Enter line of text")
words = line.rstrip().split()

for word in words:
    count[word] = count.get(word,0) + 1
print "Counts: ",count
