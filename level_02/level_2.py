f = open('text2.txt', 'r')

chars = {}

while True:
    char = f.readline(1)
    if len(char):
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    else:
        break

f.seek(0)

answer_chars = ''
for char in chars:
    if chars[char] == 1:
        answer_chars += char

answer = ''
while True:
    c = f.readline(1)
    if len(c):
        if c in answer_chars:
            answer += c
    else:
        break

f.close()

print answer
