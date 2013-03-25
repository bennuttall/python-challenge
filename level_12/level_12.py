evil = open('evil2.gfx','rb').read()
img1 = open('L12img1.jpg','wb')
img2 = open('L12img2.jpg','wb')
img3 = open('L12img3.jpg','wb')
img4 = open('L12img4.jpg','wb')
img5 = open('L12img5.jpg','wb')

for i in range(0,len(evil)-5,5):
    img1.write(evil[i])
    img2.write(evil[i+1])
    img3.write(evil[i+2])
    img4.write(evil[i+3])
    img5.write(evil[i+4])

img1.close()
img2.close()
img3.close()
img4.close()
img5.close()
