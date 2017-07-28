import urllib
import json

total = 0
url = raw_input("Enter Location: ") #http://python-data.dr-chuck.net/comments_365479.json
print "Retrieving",url
uh = urllib.urlopen(url)
data = uh.read()
print "Retrieved",len(data),"characters"

info = json.loads(data)
print "Count:",len(info)

for i in info["comments"]:
    total = total + int(i["count"])
print "Sum:",total
