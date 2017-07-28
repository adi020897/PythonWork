import urllib

uh = urllib.urlopen('http://python-data.dr-chuck.net/comments_365475.xml')

for uline in uh:
    print uline.strip()
