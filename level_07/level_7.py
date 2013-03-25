import Image

img = Image.open('oxygen.png')

box = (0,43,608,44)
img = img.crop(box)

im = img.load()

str1 = ''
for i in range(0,608,7):
    str1 += chr(im[i,0][0])

print str1

str2 = ''
# given [105, 110, 116, 101, 103, 114, 105, 116, 121]
nxt = (105, 110, 116, 101, 103, 114, 105, 116, 121)
for i in nxt:
    str2 += chr(i)

print str2
