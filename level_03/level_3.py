import re

with open('text3.txt') as f:
    text = f.read()

matches = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', text)

print(''.join(m[4] for m in matches))
