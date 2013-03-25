import zipfile
f = zipfile.ZipFile('channel.zip','r')

n = 90052
loop = 0
comments = ''

while 1:
    fn = str(n) + '.txt'
    read = f.read(fn)
    comments += f.getinfo(fn).comment
    n = read[16:]
    try:
        n = int(n)
    except:
        break

print comments
