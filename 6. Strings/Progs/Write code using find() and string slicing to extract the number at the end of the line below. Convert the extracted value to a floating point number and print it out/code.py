text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
string = text[pos:]
x = float(string)
print x