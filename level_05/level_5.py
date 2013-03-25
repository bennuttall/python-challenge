from pickle import load

f = open('banner.p', 'r')
data = load(f)

for row in data:
    r = ''
    for tup in row:
        char, n = tup
        r += n * char
    print r
