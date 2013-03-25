f = open('text3.txt','r')

low = range(96,123)
upp = range(64,91)

ans = ''
while 1:
  c = f.readline()
  if len(c):
    for i in range(73):
      if ord(c[i]) in low and all([ord(j) in upp for j in c[i+1:i+4]]) and ord(c[i+4]) in low and all([ord(j) in upp for j in c[i+5:i+8]]) and ord(c[i+8]) in low:
        ans += c[i+4]
  else:
    break
            
f.close()
print ans
