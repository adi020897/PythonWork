import urllib
import xml.etree.ElementTree as ET

total = 0
url = raw_input("Enter Location: ") #http://python-data.dr-chuck.net/comments_365475.xml
print "Retrieving",url
uh = urllib.urlopen(url)
data = uh.read()
print "Retrieved",len(data),"characters"

tree = ET.fromstring(data)
lst = tree.findall('.//count')
print "Count:",len(lst)
for item in lst:
    total = total + int(item.text)

print "Sum:",total

