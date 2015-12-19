text = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj.
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_alphabet = alphabet[2:] + alphabet[:2]

trans = str.maketrans(alphabet, new_alphabet)

print(text.translate(trans))
