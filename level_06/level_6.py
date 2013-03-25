from zipfile import ZipFile

f = ZipFile('channel.zip', 'r')

n = 90052
comments = ''

while True:
    fn = str(n) + '.txt'
    read = f.read(fn)
    comments += f.getinfo(fn).comment
    n = read[16:]
    try:
        n = int(n)
    except:
        break

print comments
