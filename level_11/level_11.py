import Image

img = Image.open('cave.jpg')

im1 = []
im2 = []
im3 = []
im4 = []

for i in range(640):
  m1 = []
  m2 = []
  m3 = []
  m4 = []
  for j in range(480):
    xy = (i,j)
    if i%2:
      if j%2:
        m1.append(img.getpixel(xy))
      else: 
        m2.append(img.getpixel(xy))
    elif j%2:
      m3.append(img.getpixel(xy))
    else:
      m4.append(img.getpixel(xy))
  if m1:
    im1.append(m1)
  if m2:
    im2.append(m2)
  if m3:
    im3.append(m3)
  if m4:
    im4.append(m4)

size = (len(im1),len(im1[0]))
img1 = Image.new('RGB',size)
img2 = Image.new('RGB',size)
img3 = Image.new('RGB',size)
img4 = Image.new('RGB',size)

x = 0
for i in im1:
  y = 0
  for j in i:
    col = j
    pos = (x,y)
    img1.putpixel(pos,col)
    y += 1
  x += 1

x = 0
for i in im2:
  y = 0
  for j in i:
    col = j
    pos = (x,y)
    img2.putpixel(pos,col)
    y += 1
  x += 1

x = 0
for i in im3:
  y = 0
  for j in i:
    col = j
    pos = (x,y)
    img3.putpixel(pos,col)
    y += 1
  x += 1

x = 0
for i in im4:
  y = 0
  for j in i:
    col = j
    pos = (x,y)
    img4.putpixel(pos,col)
    y += 1
  x += 1

img1.save('img1.jpg','jpeg')
img2.save('img2.jpg','jpeg')
img3.save('img3.jpg','jpeg')
img4.save('img4.jpg','jpeg')
