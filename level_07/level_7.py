import Image

img = Image.open('oxygen.png')

box = (0, 43, 608, 44)
img = img.crop(box)

image = img.load()

answer_1 = ''
for i in range(0, 608, 7):
    answer_1 += chr(image[i, 0][0])

print answer_1

answer_2 = ''
# given [105, 110, 116, 101, 103, 114, 105, 116, 121]
nxt = (105, 110, 116, 101, 103, 114, 105, 116, 121)
for i in nxt:
    answer_2 += chr(i)

print answer_2
