from urllib2 import urlopen

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
n = '12345'

while True:
    urln = url + n
    nxt = urlopen(urln).read()
    #print nxt
    n = ''
    for i in range(len(nxt)):
        try:
            if nxt[i: i + 24] == 'and the next nothing is ':
                n = nxt[i + 24:]
        except:
            pass
    if n == '':
        if nxt == 'Yes. Divide by two and keep going.':
            n = str(92118 / 2)
        else:
            break

print nxt
