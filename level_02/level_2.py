with open('text2.txt', 'r') as f:
    text = f.read()

chars_set = set(text)

ans = ''

for char in text:
    if char in chars_set:
        chars_set.remove(char)
        if text.count(char) == 1:
            ans += char

print(ans)
