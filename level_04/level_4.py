import urllib

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
n = '12345'

while 1:
    urln = url + n
    nxt = urllib.urlopen(urln).read()
    #print nxt
    n = ''
    for i in range(len(nxt)):
        try:
            if nxt[i:i+24] == 'and the next nothing is ':
                n = nxt[i+24:]
        except:
            pass
    if n == '':
        if nxt == 'Yes. Divide by two and keep going.':
            n = str(92118/2)
        else:
            #print nxt
            break
