f = open('text3.txt', 'r')

answer = ''
while True:
    line = f.readline()
    if len(line):
        for i in range(4, len(line) - 4):
            before_before = line[i - 4]
            before = line[i - 3: i]
            mid = line[i]
            after = line[i + 1: i + 4]
            after_after = line[i + 4]
            if (before_before.islower() and before.isupper() and mid.islower()
            and after.isupper() and after_after.islower()):
                answer += mid
    else:
        break

f.close()

print answer
