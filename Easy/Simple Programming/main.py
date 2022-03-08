with open('data.dat', 'r') as f:
    data = f.read()
    data = data.split("\n")


values = ''

lines = 0
for value in data:
    zeros = value.count('0')
    ones = value.count('1')

    if zeros == 0 and ones == 0:
        continue

    if zeros % 3 == 0 or ones % 2 == 0:
        lines += 1

print("CTFLearn{" + str(lines) + "}")