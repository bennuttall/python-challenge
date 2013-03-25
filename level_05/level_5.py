import pickle

f = open('banner.p','rb')
load = pickle.load(f)

for row in load:
    print row

s = ''

for i in load:
  for j in i:
    s += j[0]*j[1]
  s += '\n'

print s
