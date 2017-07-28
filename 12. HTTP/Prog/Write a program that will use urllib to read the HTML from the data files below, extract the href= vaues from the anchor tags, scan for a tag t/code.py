import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')          #Enter http://python-data.dr-chuck.net/known_by_Milley.html
tcon = raw_input('Enter count: ')       #Enter 7
tpos = raw_input('Enter postition: ')   #Enter 18
con = int(tcon)
pos = int(tpos)
print url

for count in range(con):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[pos-1].get('href', None)
    print url
