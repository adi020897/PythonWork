fh = open('text.txt')
count = dict()
for line in fh:
    words = line.split()
    for word in words:
        count[word] = count.get(word , 0) + 1

lst = list()
for key, val in count.items():
    lst.append((val ,key))

lst.sort(reverse=True)

for val,key in lst[:10]:
    print key,val
