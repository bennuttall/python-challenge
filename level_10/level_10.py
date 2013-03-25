a = [1]

for i in range(31):
    b = str(a[i])
    p = ''
    str1 = ''
    c = 1
    for j in range(len(b)):
        if b[j] == p:
            c += 1
        else:
            if j > 0:
                str1 += str(c) + p
            c = 1
            p = b[j]
        if j == len(b)-1:
            str1 += str(c) + p
    a.append(str1)

print len(a[30])
