from PIL import Image

moz = Image.open('mozart.gif')

w, h = moz.size
mode = moz.mode

new = Image.new(mode, (w, h))

magenta = 195

for y in range(h):
    row = [moz.getpixel((x, y)) for x in range(w)]
    i = row.index(magenta)
    new_row = row[i:] + row[:i]
    for x, px in enumerate(new_row):
        new.putpixel((x, y), px)

new.save('new.gif')  # romance
